from flask import Flask, jsonify, request
from flask_cors import CORS
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
from flask_restx import Api
from app.controllers.role_controller import role_bp
from app.config import DevelopmentConfig, ProductionConfig
from app.controllers import __blueprints__, register_namespaces
from app.utils.error_handler import handle_error
from werkzeug.middleware.proxy_fix import ProxyFix
from os import environ

app = Flask(__name__)
api = Api(app)

app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

for blueprint in __blueprints__:
    app.register_blueprint(blueprint, url_prefix=f'/{blueprint.name}')

app.register_blueprint(role_bp)

register_namespaces(api)

sentry_sdk.init(
    dsn="https://e480b614df5bbb750dd5e3d1a5d36218@o4507218437341184.ingest.us.sentry.io/4507233259159552",
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
)

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

@app.route('/endpoint', methods=['POST'])
def handle_post_request():
    json_data = request.get_json()
    if 'status' in json_data:
        status_value = json_data['status']
    return jsonify({"message": "Solicitud recibida correctamente"})

def create_app(config_name):
    app = Flask(__name__)

    if config_name == 'development':
        app.config.from_object(DevelopmentConfig)
    else:
        app.config.from_object(ProductionConfig)

    db.init_app(app)
    bcrypt_instance.init_app(app)

    with app.app_context():
        db.create_all()

    return app

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'message': 'pong'})