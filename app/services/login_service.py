import traceback
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError
from sqlalchemy import text
from app.extensions import db, bcrypt_instance
from app.models.login import Login
from app.utils.utilities import timeNowTZ
from app.schemas.login_schema import LoginSchema
from app.utils.error_handler import handle_error


def get_all():
    """
    Función para obtener todos los usuarios activos.

    Retorna:
    - list or None: Una lista de diccionarios que representan los usuarios activos si la operación es exitosa, o None si ocurre un error.
    """
    try:
        # Consulta todos los usuarios activos en la base de datos
        login_objects = db.session.query(Login).filter(Login.status == True).all()
        print("Usuarios recuperados de la base de datos:", login_objects)  # Verifica los usuarios recuperados
        # Serializa los objetos de usuario en una lista de diccionarios utilizando el esquema de usuario (UserSchema)
        login_list = LoginSchema(many=True).dump(login_objects)
        print("Lista de usuarios serializados:", login_list)  # Verifica la lista de usuarios serializados
        return login_list  # Devuelve la lista de usuarios serializados
    except Exception as e:  # Captura cualquier excepción que ocurra durante la ejecución del bloque try
        print(f"Error al obtener usuarios: {str(e)}")  # Imprime el mensaje de error
        traceback.print_exc()  # Imprimir la traza completa de la excepción
        return None  # Devuelve None para indicar que ocurrió un error durante la operación

def exists(identification: str):
    login_objects = (
        db.session.query(Login)
        .filter(Login.identification == identification, Login.status == True)
        .first()
    )
    return login_objects is not None

def create(identification: str, name: str, lastname: str, manager_id: int, password: str = None):
    try:
        if password is None:
            password = identification 
                
        new_login = Login(
            identification = identification,
            name=name,
            lastname=lastname,
            password=bcrypt_instance.generate_password_hash(password).decode("utf8"),
            manager_id=manager_id,
            status=True
        )
        db.session.add(new_login)

        db.session.commit()
        login_list = LoginSchema(exclude=["password"]).dump(new_login)
        return login_list

    except IntegrityError as ie:
        db.session.rollback()
        raise ValidationError("Error de integridad: " + str(ie.orig))

    except ValidationError as ve:
        raise ve

    except Exception as e:
        print(f"Error al crear usuario: {str(e)}")
        traceback.print_exc()
        return None
