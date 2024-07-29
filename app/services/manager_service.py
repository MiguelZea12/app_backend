import traceback
from sqlalchemy import text
from app.extensions import db
from app.models.manager import Manager
from app.schemas.manager_schema import ManagerSchema

def get_all_managers():
    """
    Función para obtener todos los gestores.

    Retorna:
    - list or None: Una lista de diccionarios que representan los gestores si la operación es exitosa, o None si ocurre un error.
    """
    try:
        # Consulta todos los managers en la base de datos
        manager_objects = db.session.query(Manager).all()
        print("Managers recuperados de la base de datos:", manager_objects)  # Verifica los managers recuperados
        # Serializa los objetos de manager en una lista de diccionarios utilizando el esquema de manager (ManagerSchema)
        manager_list = ManagerSchema(many=True).dump(manager_objects)
        print("Lista de managers serializados:", manager_list)  # Verifica la lista de managers serializados
        return manager_list  # Devuelve la lista de managers serializados
    except Exception as e:  # Captura cualquier excepción que ocurra durante la ejecución del bloque try
        print(f"Error al obtener managers: {str(e)}")  # Imprime el mensaje de error
        traceback.print_exc()  # Imprimir la traza completa de la excepción
        return None  # Devuelve None para indicar que ocurrió un error durante la operación


def toggle_manager_status(identity_document, new_status):
    """
    Función para cambiar el estado de un gestor.

    Parámetros:
    - identity_document (str): Documento de identidad del manager a actualizar.
    - new_status (bool): Nuevo estado del manager.

    Retorna:
    - dict or None: Diccionario que representa el manager actualizado si la operación es exitosa, o None si ocurre un error.
    """
    try:
        manager = db.session.query(Manager).filter(Manager.identity_document == identity_document).first()
        if not manager:
            print(f"Manager con documento de identidad {identity_document} no encontrado.")
            return None
        
        manager.status = new_status
        db.session.commit()

        manager_schema = ManagerSchema()
        manager_data = manager_schema.dump(manager)
        return manager_data
    except Exception as e:
        print(f"Error al actualizar el estado del manager: {str(e)}")
        traceback.print_exc()
        return None



def create_manager(data):
    """
    Función para crear un nuevo manager.

    Parámetros:
    - data (dict): Diccionario con los datos del manager a crear.

    Retorna:
    - dict or None: Diccionario que representa el manager creado si la operación es exitosa, 
      o un diccionario con un mensaje de error si ocurre un error.
    """
    try:
        # Validar y deserializar los datos de entrada
        new_manager_data = ManagerSchema().load(data)
        
        # Verificar si ya existe un manager con el mismo documento de identidad
        existing_manager = db.session.query(Manager).filter_by(identity_document=new_manager_data['identity_document']).first()
        if existing_manager:
            return {"error": "El manager con este documento de identidad ya existe."}
        
        # Crear un nuevo manager con los datos deserializados
        new_manager = Manager(
            first_name=new_manager_data['first_name'],
            last_name=new_manager_data['last_name'],
            identity_document=new_manager_data['identity_document'],
            gender=new_manager_data['gender'],
            age=new_manager_data['age'],
            major=new_manager_data['major'],
            semester=new_manager_data['semester'],
            city_of_residence=new_manager_data['city_of_residence'],
            team_id=new_manager_data['team_id'],
            status=True  # Asignar el estado inicial como True (activo)
        )
        
        # Agregar el nuevo manager a la sesión y hacer commit
        db.session.add(new_manager)
        db.session.commit()

        # Serializar los datos del nuevo manager
        manager_data = ManagerSchema().dump(new_manager)
        return manager_data
    except Exception as e:
        print(f"Error al crear el manager: {str(e)}")
        traceback.print_exc()
        return {"error": "Ocurrió un error al crear el manager."}
    

def update_manager(manager_id, data):
    """
    Función para actualizar un manager existente.

    Parámetros:
    - manager_id (int): ID del manager a actualizar.
    - data (dict): Diccionario con los datos del manager a actualizar.

    Retorna:
    - dict or None: Diccionario que representa el manager actualizado si la operación es exitosa, o None si ocurre un error.
    """
    try:
        # Obtener el manager por ID
        manager = db.session.query(Manager).filter(Manager.id == manager_id).first()
        if not manager:
            print(f"Manager con ID {manager_id} no encontrado.")
            return None
        
        # Actualizar los campos del manager
        manager.first_name = data.get('first_name', manager.first_name)
        manager.last_name = data.get('last_name', manager.last_name)
        manager.identity_document = data.get('identity_document', manager.identity_document)
        manager.gender = data.get('gender', manager.gender)
        manager.age = data.get('age', manager.age)
        manager.major = data.get('major', manager.major)
        manager.semester = data.get('semester', manager.semester)
        manager.city_of_residence = data.get('city_of_residence', manager.city_of_residence)
        
        # Guardar los cambios en la base de datos
        db.session.commit()

        # Serializar los datos del manager actualizado
        manager_schema = ManagerSchema()
        manager_data = manager_schema.dump(manager)
        return manager_data
    except Exception as e:
        print(f"Error al actualizar el manager: {str(e)}")
        traceback.print_exc()
        return None
    

def get_manager_by_identity_document(identity_document):
    """
    Función para obtener un manager por su número de identificación.

    Parámetros:
    - identity_document (str): Número de identificación del manager.

    Retorna:
    - dict or None: Diccionario que representa el manager si se encuentra, o None si no se encuentra.
    """
    try:
        manager = db.session.query(Manager).filter(Manager.identity_document == identity_document).first()
        if not manager:
            return None
        
        manager_schema = ManagerSchema()
        manager_data = manager_schema.dump(manager)
        return manager_data
    except Exception as e:
        print(f"Error al obtener manager por número de identificación: {str(e)}")
        traceback.print_exc()
        return None