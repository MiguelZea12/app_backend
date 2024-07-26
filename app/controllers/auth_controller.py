from flask import Blueprint, request, jsonify
from flask_restx import Api, Resource, Namespace
from app.utils.response import create_response
from app.services import auth_service

auth_blueprint = Blueprint("auth", __name__, url_prefix="/auth")
auth_ns = Namespace("auth", description="Authentication operations")
api = Api(auth_blueprint)
api.add_namespace(auth_ns)

@auth_ns.route("/login")
class Login(Resource):
    def post(self):
        """Iniciar sesión de un usuario"""
        json_data = request.get_json(force=True)
        username = json_data.get("username")
        password = json_data.get("password")

        if not username or not password:
            return create_response(
                "error", data={"message": "Username and password are required"}, status_code=400
            )

        result = auth_service.login(username, password)
        
        if result is None:
            return create_response(
                "error", data={"message": "Not found, see the credentials"}, status_code=401
            )
        
        return create_response("success", data=result, status_code=200)
