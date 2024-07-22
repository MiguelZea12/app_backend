import traceback
from flask import Blueprint, request, jsonify
from flask_restx import Api, Resource, Namespace, fields

from app.services import manager_service
from app.schemas.manager_schema import ManagerSchema

manager_blueprint = Blueprint("Manager", __name__, url_prefix="/manager")
# Crea un Namespace para el blueprint
manager_ns = Namespace("Manager", description="Manager operations")

# Inicializa la extensión Api con el blueprint y el Namespace
api = Api(manager_blueprint)
api.add_namespace(manager_ns) # Agrega el Namespace al Api

# Define el esquema de usuario
manager_schema = ManagerSchema()

# Definición del modelo de datos para la entrada
manager_model = manager_ns.model('Manager', {
    'first_name': fields.String(required=True, description='First name of the manager'),
    'last_name': fields.String(required=True, description='Last name of the manager'),
    'identity_document': fields.String(required=True, description='Identity document of the manager'),
    'gender': fields.String(required=True, description='Gender of the manager'),
    'age': fields.Integer(required=True, description='Age of the manager'),
    'major': fields.String(required=True, description='Major of the manager'),
    'semester': fields.String(required=True, description='Semester of the manager'),
    'city_of_residence': fields.String(required=True, description='City of residence of the manager')
})

# Definición del modelo de datos para la entrada de actualización de estado
status_model = manager_ns.model('StatusUpdate', {
    'status': fields.Boolean(required=True, description='New status of the manager')
})


# Define la clase para obtener todos los gestores
@manager_ns.route("/managers")
class ManagerList(Resource):
    def get(self):
        """Obtener todos los managers"""
        managers = manager_service.get_all_managers()
        print(managers) # Verificar datos devueltos por el servicio
        return managers


# Define la clase para crear un nuevo gestor
@manager_ns.route("/crear")
class ManagerCreate(Resource):
    @manager_ns.expect(manager_model)
    def post(self):
        """Crear un nuevo manager"""
        data = request.get_json()
        if not data:
            return jsonify({"error": "El cuerpo de la solicitud no puede estar vacío."}), 400
        
        new_manager = manager_service.create_manager(data)
        if "error" in new_manager:
            return new_manager, 400
        
        return new_manager, 201


# Define la clase para actualizar el estado de un gestor
@manager_ns.route("/toggle_status/<string:identity_document>")
class ManagerStatus(Resource):
    @manager_ns.expect(status_model)
    def put(self, identity_document):
        """Actualizar el estado de un manager (habilitar o deshabilitar)"""
        data = request.get_json()
        if not data:
            return jsonify({"error": "El cuerpo de la solicitud no puede estar vacío."}), 400

        new_status = data.get('status')
        if new_status is None:
            return jsonify({"error": "El campo 'status' es requerido."}), 400

        updated_manager = manager_service.toggle_manager_status(identity_document, new_status)
        if updated_manager is None:
            return jsonify({"error": "Manager no encontrado o no se pudo actualizar el estado."}), 404

        return "Se ha actualizado el estado correctamente", 200



# Define la clase para actualizar a un gestor existente
@manager_ns.route("/actualizar/<int:manager_id>")
class ManagerDetail(Resource):
    @manager_ns.expect(manager_model)
    def put(self, manager_id):
        """Actualizar un manager existente"""
        data = request.get_json()
        if not data:
            return jsonify({"error": "El cuerpo de la solicitud no puede estar vacío."}), 400

        updated_manager = manager_service.update_manager(manager_id, data)
        if updated_manager is None:
            return jsonify({"error": "Manager no encontrado o no se pudo actualizar."}), 404

        return updated_manager, 200


# Define la clase para buscar un gestor por si numero de identificacion
@manager_ns.route("/buscar/<string:identity_document>")
class ManagerByIdentityDocument(Resource):
    @manager_ns.doc('get_manager_by_identity_document')
    @manager_ns.response(200, 'Success')
    @manager_ns.response(404, 'Manager not found')
    def get(self, identity_document):
        """
        Obtener un manager por su número de identificación.

        Este endpoint permite obtener un manager por su número de identificación.
        Si el manager se encuentra, se devuelve un código de estado 200 con los datos del manager.
        Si no se encuentra, se devuelve un código de estado 404 con un mensaje de error.
        """
        manager = manager_service.get_manager_by_identity_document(identity_document)
        if manager is None:
            return jsonify({"error": "Manager no encontrado."}), 404

        return manager, 200