from app.models.caregiver import Caregiver
from app.extensions import db
from sqlalchemy.exc import IntegrityError

# Función para obtener todos los cuidadores
def get_all_caregivers():
    caregivers = Caregiver.query.all()  # Consulta todos los registros de la tabla 'caregivers'
    return [caregiver.to_dict() for caregiver in caregivers]  # Convierte cada cuidador en un diccionario y los devuelve en una lista

# Función para obtener un cuidador por su ID
def get_caregiver_by_id(id):
    caregiver = Caregiver.query.get(id)  # Busca un cuidador por su ID
    return caregiver.to_dict() if caregiver else None  # Si se encuentra el cuidador, lo convierte en un diccionario; de lo contrario, devuelve None

# Función para crear un nuevo cuidador
def create_caregiver(data):
    new_caregiver = Caregiver(**data)  # Crea una nueva instancia de Caregiver usando los datos proporcionados
    db.session.add(new_caregiver)  # Añade el nuevo cuidador a la sesión de la base de datos
    try:
        db.session.commit()  # Intenta confirmar la transacción en la base de datos
        return new_caregiver.to_dict()  # Si tiene éxito, devuelve el nuevo cuidador como un diccionario
    except IntegrityError:  # Captura errores de integridad (por ejemplo, clave duplicada)
        db.session.rollback()  # Deshace la transacción en caso de error
        return {'message': 'document_id already exists'}, 400  # Devuelve un mensaje de error

# Función para actualizar un cuidador existente
def update_caregiver(id, data):
    caregiver = Caregiver.query.get(id)  # Busca un cuidador por su ID
    if caregiver:  # Si se encuentra el cuidador
        for key, value in data.items():  # Itera sobre los pares clave-valor en los datos proporcionados
            setattr(caregiver, key, value)  # Actualiza los atributos del cuidador con los nuevos valores
        try:
            db.session.commit()  # Intenta confirmar la transacción en la base de datos
            return caregiver.to_dict()  # Si tiene éxito, devuelve el cuidador actualizado como un diccionario
        except IntegrityError:  # Captura errores de integridad
            db.session.rollback()  # Deshace la transacción en caso de error
            return {'message': 'Error updating caregiver'}, 400  # Devuelve un mensaje de error
    return None  # Si no se encuentra el cuidador, devuelve None

# Función para deshabilitar un cuidador (marcar como inactivo)
def disable_caregiver(id):
    caregiver = Caregiver.query.get(id)  # Busca un cuidador por su ID
    if caregiver:  # Si se encuentra el cuidador
        caregiver.is_active = False  # Establece el atributo 'is_active' a False
        try:
            db.session.commit()  # Intenta confirmar la transacción en la base de datos
            return caregiver.to_dict()  # Si tiene éxito, devuelve el cuidador deshabilitado como un diccionario
        except IntegrityError:  # Captura errores de integridad
            db.session.rollback()  # Deshace la transacción en caso de error
            return {'message': 'Error disabling caregiver'}, 400  # Devuelve un mensaje de error
    return None  # Si no se encuentra el cuidador, devuelve None
