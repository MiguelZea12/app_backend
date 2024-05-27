from flask import Blueprint, request
from app.utils.response import create_response
from flask_restx import Api, Resource, Namespace  # Importa Namespace de flask_restx

from app.services import user_service
from app.schemas.user_schema import UserSchema

user_blueprint = Blueprint("User", __name__, url_prefix="/user")
# Crea un Namespace para el blueprint
user_ns = Namespace("User", description="User operations")

# Inicializa la extensión Api con el blueprint y el Namespace
api = Api(user_blueprint)
api.add_namespace(user_ns)  # Agrega el Namespace al Api

# Define el esquema de usuario
user_schema = UserSchema()

# Define la clase para obtener todos los usuarios
@user_ns.route("/users")
class UserList(Resource):
    def get(self):
        """Obtener todos los usuarios"""
        users = user_service.get_all()
        print(users)  # Verificar datos devueltos por el servicio
        return users


@user_blueprint.route("/post", methods=["POST"])
def create():
    json_data = request.get_json(force=True)
    users = user_service.create(json_data)
    if users is None:
        print(users)
        return create_response(
            "error", data={"message": "Error al crear al usuario"}, status_code=500
        )
    return create_response("success", data={"usuario": users}, status_code=201)
