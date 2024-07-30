from flask import request
from flask_restx import Namespace, Resource, fields
from app.services.caregiver_service import (
    get_all_caregivers, get_caregiver_by_id, create_caregiver,
    update_caregiver, disable_caregiver
)

caregiver_ns = Namespace('Cuidadores', description='Operaciones relacionadas con los cuidadores')

caregiver_model = caregiver_ns.model('Cuidador', {
    'id': fields.Integer(readonly=True, description='El identificador único del cuidador'),
    'canton': fields.String(required=True, description='El cantón del cuidador'),
    'parish': fields.String(required=True, description='La parroquia del cuidador'),
    'zone_type': fields.String(required=True, description='El tipo de zona del cuidador'),
    'address': fields.String(required=True, description='La dirección del cuidador'),
    'reference': fields.String(description='Referencia de la dirección'),
    'landline_1': fields.String(description='Teléfono fijo 1'),
    'landline_2': fields.String(description='Teléfono fijo 2'),
    'mobile_1': fields.String(description='Teléfono móvil 1'),
    'mobile_2': fields.String(description='Teléfono móvil 2'),
    'caregiver_document_id': fields.String(required=True, description='El ID del documento del cuidador'),
    'caregiver_last_name': fields.String(required=True, description='El apellido del cuidador'),
    'caregiver_first_name': fields.String(required=True, description='El nombre del cuidador'),
    'caregiver_gender': fields.String(required=True, description='El género del cuidador'),
    'relationship': fields.String(required=True, description='La relación con el usuario'),
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
        return create_caregiver(data)

@caregiver_ns.route('/cuidadores/<int:id>')
@caregiver_ns.response(404, 'Cuidador no encontrado')
@caregiver_ns.param('id', 'El identificador del cuidador')
class Caregiver(Resource):
    @caregiver_ns.doc('obtener_cuidador')
    @caregiver_ns.marshal_with(caregiver_model)
    def get(self, id):
        """Obtener un cuidador dado su id"""
        result = get_caregiver_by_id(id)
        if not result:
            caregiver_ns.abort(404, 'Cuidador no encontrado')
        return result

    @caregiver_ns.doc('eliminar_cuidador')
    @caregiver_ns.response(204, 'Cuidador eliminado')
    def delete(self, id):
        """Eliminar un cuidador dado su id"""
        result = disable_caregiver(id)
        if not result:
            caregiver_ns.abort(404, 'Cuidador no encontrado')
        return '', 204

    @caregiver_ns.expect(caregiver_model)
    @caregiver_ns.marshal_with(caregiver_model)
    def put(self, id):
        """Actualizar un cuidador dado su id"""
        data = request.json
        result = update_caregiver(id, data)
        if not result:
            caregiver_ns.abort(404, 'Cuidador no encontrado')
        return result