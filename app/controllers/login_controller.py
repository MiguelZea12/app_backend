from flask import Blueprint, request, jsonify
from app.utils.response import create_response
from flask_restx import Api, Resource, Namespace  # Importa Namespace de flask_restx

from app.services import login_service
from app.schemas.login_schema import LoginSchema

login_blueprint = Blueprint("login", __name__, url_prefix="/login")
# Crea un Namespace para el blueprint
login_ns = Namespace("login", description="Login operations")

# Inicializa la extensión Api con el blueprint y el Namespace
api = Api(login_blueprint)
api.add_namespace(login_ns)  # Agrega el Namespace al Api

# Define el esquema de usuario
login_schema = LoginSchema()

# Define la clase para obtener todos los usuarios
@login_ns.route("/")
class LoginList(Resource):
    def get(self):
        """Obtener todos los usuarios logiados"""
        users = login_service.get_all()
        print(users)  # Verificar datos devueltos por el servicio
        return create_response("success", data={"users": users}, status_code=200)

    def post(self):
        """Crear un nuevo usuario para logearse"""
        json_data = request.get_json(force=True)
        password = json_data.get("password") # Obtener la contraseña del JSON, puede ser None

        new_login = login_service.create(
            json_data["identification"],
            json_data["name"],
            json_data["lastname"],
            password
        )
        if new_login is None:
            return create_response("error", data={"message": "Error creating the login user"}, status_code=500)

        return create_response("success", data={"user": new_login}, status_code=201)
