from flask import Flask, jsonify, request
from flask_cors import CORS
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
from flask_restx import Api
from app.controllers.role_controller import role_bp  # Importa el blueprint de roles
from app.controllers import __blueprints__, register_namespaces
from app.utils.error_handler import handle_error
from werkzeug.middleware.proxy_fix import ProxyFix
from os import environ

app = Flask(__name__)  # Crea una instancia de la aplicación Flask
api = Api(app)  # Crea una instancia de la clase Api de Flask-Restx

app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

# Registra todos los blueprints encontrados
for blueprint in __blueprints__:
    app.register_blueprint(blueprint, url_prefix=f'/{blueprint.name}')  # Añade url_prefix

# Registra el blueprint de roles con un nombre único
app.register_blueprint(role_bp)

# Registra namespaces
register_namespaces(api)

# Implementación de sentry para manejo de errores
sentry_sdk.init(
    dsn="https://e480b614df5bbb750dd5e3d1a5d36218@o4507218437341184.ingest.us.sentry.io/4507233259159552",
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
)

# Configuración de la aplicación según el entorno (producción o desarrollo)
if environ.get("ENVIRONMENT") == "PROD":
    app.config.from_object("app.config.ProductionConfig")
else:
    app.config.from_object("app.config.DevelopmentConfig")

CORS(app)

# Configuración de la aplicación Flask
with app.app_context():
    # Importa extensiones y modelos dentro del contexto de la aplicación
    from app.extensions import db, jwt, bcrypt_instance
    from app.models.declarative_base import DeclarativeBase
    from app.models import *
    from app.controllers import *

    app.register_error_handler(Exception, handle_error)

    db.init_app(app)
    jwt.init_app(app)
    bcrypt_instance.init_app(app)

    DeclarativeBase.metadata.create_all(db.engine, checkfirst=True)

# Define un endpoint de ejemplo para manejar solicitudes POST
@app.route('/endpoint', methods=['POST'])
def handle_post_request():
    json_data = request.get_json()
    print("JSON recibido:", json_data)
    if 'status' in json_data:
        status_value = json_data['status']
        print("Valor de 'status':", status_value)
    else:
        print("La clave 'status' no está presente en el JSON recibido")
    return jsonify({"message": "Solicitud recibida correctamente"})

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'message': 'pong'})
