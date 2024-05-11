import traceback
from sqlalchemy import text
from app.extensions import db, bcrypt_instance
from app.models.user import User
from app.utils.utilities import timeNowTZ
from app.schemas.user_schema import UserSchema


def get_all():
    """
    Función para obtener todos los usuarios activos.

    Retorna:
    - list or None: Una lista de diccionarios que representan los usuarios activos si la operación es exitosa, o None si ocurre un error.
    """
    try:
        # Consulta todos los usuarios activos en la base de datos
        user_objects = db.session.query(User).filter(User.status == True).all()
        print("Usuarios recuperados de la base de datos:", user_objects)  # Verifica los usuarios recuperados
        # Serializa los objetos de usuario en una lista de diccionarios utilizando el esquema de usuario (UserSchema)
        user_list = UserSchema(many=True).dump(user_objects)
        print("Lista de usuarios serializados:", user_list)  # Verifica la lista de usuarios serializados
        return user_list  # Devuelve la lista de usuarios serializados
    except Exception as e:  # Captura cualquier excepción que ocurra durante la ejecución del bloque try
        print(f"Error al obtener usuarios: {str(e)}")  # Imprime el mensaje de error
        traceback.print_exc()  # Imprimir la traza completa de la excepción
        return None  # Devuelve None para indicar que ocurrió un error durante la operación
