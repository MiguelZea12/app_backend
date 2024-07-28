from flask import Blueprint, request, jsonify
from app.utils.response import create_response
from flask_restx import Api, Resource, Namespace

from app.services import login_service
from app.schemas.login_schema import LoginSchema

login_usr_blueprint = Blueprint("login", __name__, url_prefix="/login")
login_ns = Namespace("login", description="Login operations")

api = Api(login_usr_blueprint)
api.add_namespace(login_ns)

login_schema = LoginSchema()

@login_ns.route("/logins")
class LoginList(Resource):
    def get(self):
        """Obtener todos los usuarios logiados"""
        logins = login_service.get_all()
        print(logins)
        return create_response("success", data={"logins": logins}, status_code=200)

    def post(self):
        """Crear un nuevo usuario para logearse"""
        json_data = request.get_json(force=True)
        password = json_data.get("password")

        new_login = login_service.create(
            json_data["identification"],
            json_data["name"],
            json_data["lastname"],
            password
        )
        if new_login is None:
            return create_response("error", data={"message": "Error creating the login user"}, status_code=500)

        return create_response("success", data={"login": new_login}, status_code=201)

@login_ns.route("/logins/<int:login_id>")
class LoginDetail(Resource):
    def get(self, login_id):
        login = login_service.get_by_id(login_id)
        if login:
            return jsonify(login)
        return jsonify({"message": "Login user not found"}), 404
    
    def put(self, login_id):
        data = request.get_json()
        updated_login = login_service.update(login_id, data)
        if updated_login:
            return jsonify(updated_login)
        return jsonify({"message": "Login user not found"}), 404
