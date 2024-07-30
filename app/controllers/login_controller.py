from flask import Blueprint, request, jsonify
from app.utils.response import create_response
from flask_restx import Api, Resource, Namespace
from marshmallow import ValidationError

from app.services import login_service
from app.schemas.login_schema import LoginSchema

login_blueprint = Blueprint("login", __name__, url_prefix="/login")
login_ns = Namespace("login", description="Login operations")

api = Api(login_blueprint)
api.add_namespace(login_ns)

login_schema = LoginSchema()

@login_ns.route("/")
class LoginList(Resource):
    def get(self):
        """Obtener todos los usuarios logiados"""
        users = login_service.get_all()
        return create_response("success", data={"users": users}, status_code=200)

    def post(self):
        """Crear un nuevo usuario para logearse"""
        try:
            json_data = request.get_json(force=True)
            password = json_data.get("password")

            new_login = login_service.create(
                json_data["identification"],
                json_data["name"],
                json_data["lastname"],
                json_data["manager_id"],
                password
            )
            return create_response("success", data={"user": new_login}, status_code=201)

        except ValidationError as ve:
            return create_response("error", data={"message": str(ve)}, status_code=400)

        except Exception as e:
            return create_response("error", data={"message": str(e)}, status_code=500)

@login_ns.route("/authenticate")
class LoginAuthenticate(Resource):
    def post(self):
        """Autenticar un usuario"""
        try:
            json_data = request.get_json(force=True)
            token_data = login_service.authenticate(
                json_data["identification"],
                json_data["password"]
            )
            if token_data:
                return create_response("success", data=token_data, status_code=200)
            else:
                return create_response("error", data={"message": "Credenciales inválidas"}, status_code=401)

        except Exception as e:
            return create_response("error", data={"message": str(e)}, status_code=500)
