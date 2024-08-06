from flask import Blueprint, request, jsonify
from flask_restx import Api, Resource, Namespace, fields

from app.services import assignmentUser_service
from app.schemas.assignmentUser_schema import AssignmentUserSchema

assignmentUser_blueprint = Blueprint("AssignmentUser", __name__, url_prefix="/assignments")
assignment_ns = Namespace("AssignmentUser", description="Assignment operations")

api = Api(assignmentUser_blueprint)
api.add_namespace(assignment_ns)

assignment_schema = AssignmentUserSchema()

assignment_model = assignment_ns.model('AssignmentUser', {
    'login_id': fields.Integer(required=True, description='ID del usuario que se va a asignar'),
    'team_id': fields.Integer(required=True, description='ID del equipo al que se va a asignar')
})

@assignment_ns.route("/")
class AssignmentUserList(Resource):
    @assignment_ns.doc('get_all_assignments')
    @assignment_ns.response(200, 'Success')
    @assignment_ns.response(500, 'Internal Server Error')
    def get(self):
        """
        Obtener todas las asignaciones
        """
        assignments = assignmentUser_service.get_all_assignments()
        if assignments is None:
            return jsonify({"error": "Ocurrió un error al obtener las asignaciones."}), 500
        return assignments, 200

@assignment_ns.route("/team/<int:team_id>")
class AssignmentUserByTeam(Resource):
    @assignment_ns.doc('get_assignments_by_team_id')
    @assignment_ns.response(200, 'Success')
    @assignment_ns.response(404, 'Assignments not found')
    def get(self, team_id):
        """
        Obtener todas las asignaciones por ID de equipo
        """
        assignments = assignmentUser_service.get_assignments_by_team_id(team_id)
        if assignments is None:
            return jsonify({"error": "No se encontraron asignaciones para el equipo especificado."}), 404
        return assignments, 200

@assignment_ns.route("/crear")
class AssignmentUserCreate(Resource):
    @assignment_ns.expect(assignment_model)
    @assignment_ns.response(201, 'Created')
    @assignment_ns.response(400, 'Bad Request')
    def post(self):
        """
        Crear una nueva asignación
        """
        data = request.get_json()
        if not data:
            return jsonify({"error": "El cuerpo de la solicitud no puede estar vacío."}), 400
        
        new_assignment = assignmentUser_service.create_assignment(data)
        if "error" in new_assignment:
            return new_assignment, 400
        
        return new_assignment, 201

@assignment_ns.route("/actualizar/<int:id>")
class AssignmentUserDetail(Resource):
    @assignment_ns.expect(assignment_model)
    @assignment_ns.response(200, 'Success')
    @assignment_ns.response(400, 'Bad Request')
    @assignment_ns.response(404, 'Assignment not found')
    def put(self, id):
        """
        Actualizar una asignación existente
        """
        data = request.get_json()
        if not data:
            return jsonify({"error": "El cuerpo de la solicitud no puede estar vacío."}), 400

        updated_assignment = assignmentUser_service.update_assignment(id, data)
        if updated_assignment is None:
            return jsonify({"error": "Asignación no encontrada o no se pudo actualizar."}), 404

        return updated_assignment, 200

@assignment_ns.route("/eliminar/<int:id>")
class AssignmentUserDelete(Resource):
    @assignment_ns.doc('delete_assignment')
    @assignment_ns.response(200, 'Success')
    @assignment_ns.response(404, 'Assignment not found')
    def delete(self, id):
        """
        Eliminar una asignación existente
        """
        result = assignmentUser_service.delete_assignment(id)
        if "error" in result:
            return jsonify(result), 500
        return result, 200
