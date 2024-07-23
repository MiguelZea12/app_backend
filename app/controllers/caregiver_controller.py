from flask import request
from flask_restx import Namespace, Resource, fields
from app.services.caregiver_service import (
    get_all_caregivers, get_caregiver_by_id, create_caregiver,
    update_caregiver, disable_caregiver
)

caregiver_ns = Namespace('Cuidadores', description='Operaciones relacionadas con los cuidadores')

caregiver_model = caregiver_ns.model('Cuidador', {
    'id': fields.Integer(readonly=True, description='El identificador único del cuidador'),
    'name': fields.String(required=True, description='El nombre del cuidador'),
    'document_id': fields.String(required=True, description='El ID del documento del cuidador'),
    'gender': fields.String(required=True, description='El género del cuidador'),
    'age': fields.Integer(required=True, description='La edad del cuidador'),
    'career': fields.String(required=True, description='La carrera del cuidador'),
    'semester': fields.String(required=True, description='El semestre del cuidador'),
    'city': fields.String(required=True, description='La ciudad del cuidador'),
    'is_active': fields.Boolean(readonly=True, description='Si el cuidador está activo')
})

@caregiver_ns.route('/cuidadores')
class CaregiverList(Resource):
    @caregiver_ns.doc('listar_cuidadores')
    @caregiver_ns.marshal_list_with(caregiver_model)
    def get(self):
        """Listar todos los cuidadores"""
        return get_all_caregivers()

    @caregiver_ns.doc('crear_cuidador')
    @caregiver_ns.expect(caregiver_model)
    @caregiver_ns.marshal_with(caregiver_model, code=201)
    def post(self):
        """Crear un nuevo cuidador"""
        data = request.json
        return create_caregiver(data), 201

@caregiver_ns.route('/cuidadores/<int:id>')
@caregiver_ns.response(404, 'Cuidador no encontrado')
@caregiver_ns.param('id', 'El identificador del cuidador')
class Caregiver(Resource):
    @caregiver_ns.doc('obtener_cuidador')
    @caregiver_ns.marshal_with(caregiver_model)
    def get(self, id):
        """Obtener un cuidador dado su id"""
        return get_caregiver_by_id(id)

    @caregiver_ns.doc('eliminar_cuidador')
    @caregiver_ns.response(204, 'Cuidador eliminado')
    def delete(self, id):
        """Eliminar un cuidador dado su id"""
        disable_caregiver(id)
        return '', 204

    @caregiver_ns.expect(caregiver_model)
    @caregiver_ns.marshal_with(caregiver_model)
    def put(self, id):
        """Actualizar un cuidador dado su id"""
        data = request.json
        return update_caregiver(id, data)
