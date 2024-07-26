from app.extensions import db, bcrypt_instance
from app.models.login import Login
from app.models.token_block_list import TokenBlockList
from flask_jwt_extended import create_access_token  # , create_refresh_token


def login(username: str, password: str):
    """
    Función para el proceso de inicio de sesión de un usuario.

    Parámetros:
    - username (str): Nombre de usuario del usuario que intenta iniciar sesión.
    - password (str): Contraseña proporcionada por el usuario que intenta iniciar sesión.

    Retorna:
    - dict: Un diccionario que contiene un token de acceso si las credenciales son válidas, o None si no lo son.
    """
    # Consulta el usuario en la base de datos por su nombre de usuario y estado activo
    login_object = (
        db.session.query(Login)
        .filter(Login.identification == username, Login.status == True)
        .first()
    )
    if login_object is not None:  # Si se encuentra el usuario en la base de datos
        if bcrypt_instance.check_password_hash(login_object.password, password):  # Si la contraseña proporcionada coincide con la contraseña almacenada
            # Crear un diccionario que representa la identidad del usuario para generar el token de acceso
            login_identity = {"id": login_object.id, "identification": login_object.identification}
            access_token = create_access_token(identity=login_identity)  # Generar un token de acceso usando la identidad del usuario
            # refresh_token = create_refresh_token(identity=user_identity)
            return {"access_token": access_token}  # Devolver el token de acceso
        else:  # Si la contraseña proporcionada no coincide con la contraseña almacenada
            return None  # Devolver None (credenciales inválidas)
    else:  # Si no se encuentra el usuario en la base de datos
        return None  # Devolver None (credenciales inválidas)


def logout(jti: str):
    """
    Función para el proceso de cierre de sesión de un usuario.

    Parámetros:
    - jti (str): Identificador único del token JWT que se va a bloquear.

    Retorna:
    - bool: True si el token se bloquea correctamente, False si no se puede bloquear.
    """
    token_block_list = TokenBlockList(jti)  # Crear una instancia de TokenBlockList con el identificador único del token JWT
    db.session.add(token_block_list)  # Agregar la instancia de TokenBlockList a la sesión de la base de datos
    db.session.commit()  # Confirmar los cambios en la base de datos
    return True  # Devolver True (cierre de sesión exitoso)
