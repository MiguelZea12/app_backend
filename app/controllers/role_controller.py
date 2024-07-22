from flask import Blueprint, request, jsonify
from flask_restx import Api, Resource, Namespace

from app.services.role_service import RoleService
from app.schemas.role_schema import RoleSchema

# Crea un Blueprint para los roles
role_bp = Blueprint("role_bp", __name__, url_prefix="/role")
# Crea un Namespace para el blueprint
role_ns = Namespace("Role", description="Role operations")

# Inicializa la extensión Api con el blueprint y el Namespace
api = Api(role_bp)
api.add_namespace(role_ns)

# Define el esquema de roles
role_schema = RoleSchema()
roles_schema = RoleSchema(many=True)

# Define la clase para obtener todos los roles
@role_ns.route("/roles")
class RoleList(Resource):
    def get(self):
        """Obtener todos los roles"""
        roles = RoleService.get_all_roles()
        result = roles_schema.dump(roles)
        return result, 200

    def post(self):
        """Crear un nuevo rol"""
        data = request.get_json()
        errors = role_schema.validate(data)
        if errors:
            return jsonify(errors), 400
        role, error = RoleService.create_role(data)
        if error:
            return jsonify({'message': error}), 400
        result = role_schema.dump(role)
        return result, 201

# Define la clase para obtener, actualizar y eliminar un rol por ID
@role_ns.route("/roles/<int:role_id>")
class Role(Resource):
    def get(self, role_id):
        """Obtener un rol por ID"""
        role = RoleService.get_role_by_id(role_id)
        if not role:
            return jsonify({'message': 'Role not found'}), 404
        result = role_schema.dump(role)
        return result, 200

    def put(self, role_id):
        """Actualizar un rol por ID"""
        role = RoleService.get_role_by_id(role_id)
        if not role:
            return jsonify({'message': 'Role not found'}), 404
        data = request.get_json()
        errors = role_schema.validate(data)
        if errors:
            return jsonify(errors), 400
        role = RoleService.update_role(role, data)
        result = role_schema.dump(role)
        return result, 200

    def delete(self, role_id):
        """Eliminar un rol por ID"""
        role = RoleService.get_role_by_id(role_id)
        if not role:
            return jsonify({'message': 'Role not found'}), 404
        RoleService.delete_role(role)
        return '', 204
