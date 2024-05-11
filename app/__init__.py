from flask import Flask, jsonify, request
from flask_cors import CORS
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
from flask_restx import Api
from app.controllers.user_controller import user_blueprint
from app.utils.error_handler import handle_error
from os import environ

app = Flask(__name__)  # Crea una instancia de la aplicación Flask
api = Api(app)  # Crea una instancia de la clase Api de Flask-Restx

app.register_blueprint(user_blueprint)  # Registra el blueprint del controlador de usuario en la aplicación


# Implentacion de sentry para manejo de errores
sentry_sdk.init(
    dsn="https://e480b614df5bbb750dd5e3d1a5d36218@o4507218437341184.ingest.us.sentry.io/4507233259159552",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)

# Configuración de la aplicación según el entorno (producción o desarrollo)
if environ.get("ENVIRONMENT") == "PROD":  # Si la variable de entorno ENVIRONMENT es PROD
    app.config.from_object("app.config.ProductionConfig")  # Usa la configuración de producción
else:  # Si la variable de entorno ENVIRONMENT no es PROD
    app.config.from_object("app.config.DevelopmentConfig")  # Usa la configuración de desarrollo

CORS(app)  # Configura CORS para permitir solicitudes desde cualquier origen

# Configuración de la base de datos PostgreSQL
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:12345@localhost:5432/prueba'

# Configuración de la aplicación Flask
with app.app_context():
    # Importa extensiones y modelos dentro del contexto de la aplicación
    from app.extensions import db, jwt, bcrypt_instance
    from app.models.declarative_base import DeclarativeBase
    from app.models import *
    from app.controllers import *

    app.register_error_handler(Exception, handle_error)  # Registra un manejador de errores global

    db.init_app(app)  # Inicializa la extensión de base de datos
    jwt.init_app(app)  # Inicializa la extensión JWT
    bcrypt_instance.init_app(app)  # Inicializa la extensión de hash de contraseñas

    # Crea todas las tablas en la base de datos si aún no existen
    DeclarativeBase.metadata.create_all(db.engine, checkfirst=True)

# Define un endpoint de ejemplo para manejar solicitudes POST
@app.route('/endpoint', methods=['POST'])
def handle_post_request():
    # Obtener el JSON enviado en la solicitud POST
    json_data = request.get_json()

    # Imprimir el JSON recibido en la consola del servidor
    print("JSON recibido:", json_data)

    # Verificar si la clave 'status' está presente en el JSON recibido
    if 'status' in json_data:
        status_value = json_data['status']
        print("Valor de 'status':", status_value)
    else:
        print("La clave 'status' no está presente en el JSON recibido")

    # Aquí continuarías con el manejo de la solicitud POST...

    # Por ejemplo, devolver una respuesta al cliente
    return jsonify({"message": "Solicitud recibida correctamente"})
