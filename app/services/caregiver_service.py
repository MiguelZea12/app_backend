from app.models.caregiver import Caregiver
from app.extensions import db
from sqlalchemy.exc import IntegrityError
from marshmallow import ValidationError
from app.schemas.caregiver_schema import CaregiverSchema

# Función para obtener todos los cuidadores
def get_all_caregivers():
    caregivers = db.session.query(Caregiver).all()
    return CaregiverSchema(many=True).dump(caregivers)

# Función para obtener un cuidador por su ID
def get_caregiver_by_id(id):
    caregiver = Caregiver.query.get(id)
    return CaregiverSchema().dump(caregiver) if caregiver else None

# Función para crear un nuevo cuidador
def create_caregiver(data):
    schema = CaregiverSchema()
    try:
        caregiver_data = schema.load(data)
    except ValidationError as err:
        return {'message': str(err)}, 400

    new_caregiver = Caregiver(**caregiver_data)
    db.session.add(new_caregiver)
    try:
        db.session.commit()
        return schema.dump(new_caregiver)
    except IntegrityError:
        db.session.rollback()
        return {'message': 'document_id already exists'}, 400

# Función para actualizar un cuidador existente
def update_caregiver(id, data):
    caregiver = Caregiver.query.get(id)
    if not caregiver:
        return None

    schema = CaregiverSchema()
    try:
        updated_data = schema.load(data, partial=True)
    except ValidationError as err:
        return {'message': str(err)}, 400

    for key, value in updated_data.items():
        setattr(caregiver, key, value)

    try:
        db.session.commit()
        return schema.dump(caregiver)
    except IntegrityError:
        db.session.rollback()
        return {'message': 'Error updating caregiver'}, 400

# Función para deshabilitar un cuidador (marcar como inactivo)
def disable_caregiver(id):
    caregiver = Caregiver.query.get(id)
    if not caregiver:
        return None

    caregiver.is_active = False
    try:
        db.session.commit()
        return CaregiverSchema().dump(caregiver)
    except IntegrityError:
        db.session.rollback()
        return {'message': 'Error disabling caregiver'}, 400