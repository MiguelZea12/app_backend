from flask import Flask, jsonify, request
from flask_cors import CORS
from app.utils.error_handler import handle_error
from os import environ

app = Flask(__name__)

if environ.get("ENVIRONMENT") == "PROD":
    app.config.from_object("app.config.ProductionConfig")
else:
    app.config.from_object("app.config.DevelopmentConfig")
CORS(app)

with app.app_context():
    from app.extensions import db, jwt, bcrypt_instance
    from app.models.declarative_base import DeclarativeBase
    from app.models import *
    from app.controllers import *

    app.register_error_handler(Exception, handle_error)
    db.init_app(app)
    jwt.init_app(app)
    bcrypt_instance.init_app(app)
    DeclarativeBase.metadata.create_all(db.engine, checkfirst=True)


@jwt.revoked_token_loader
def revoked_token_callback(jwt_header, jwt_payload):
    from app.utils.response import create_response

    return create_response(
        "error",
        message="El Token ha sido revocado. Inicie Sesión nuevamente.",
        status_code=401,
    )


@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    from app.utils.response import create_response

    return create_response(
        "error",
        message="El Token ha caducado. Inicie Sesión nuevamente.",
        status_code=401,
    )


@jwt.invalid_token_loader
def invalid_token_callback(error):
    from app.utils.response import create_response

    return create_response(
        "error", message="Fallo en la verificación de la firma.", status_code=401
    )


@jwt.unauthorized_loader
def missing_token_callback(error):
    from app.utils.response import create_response

    return create_response(
        "error", message="La solicitud no contiene un Token de Acceso.", status_code=401
    )


@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_payload):
    from app.models.token_block_list import TokenBlockList

    jti = jwt_payload["jti"]
    token = db.session.query(TokenBlockList).filter_by(jti=jti).scalar()
    return token is not None

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
#: Registro de Blueprints
from app.controllers import __blueprints__

for blueprint in __blueprints__:
    print("Registering Blueprint: {}".format(blueprint.name))
    app.register_blueprint(blueprint)


@app.route("/", methods=["GET"])
def test():
    return "Template API-Flask"

