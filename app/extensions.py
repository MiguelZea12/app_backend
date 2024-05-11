"""Extensiones de la aplicación."""
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
import logging
from flask import has_request_context, request


# Instancias de las extensiones
db = SQLAlchemy()  # Instancia de SQLAlchemy para interactuar con la base de datos
bcrypt_instance = Bcrypt()  # Instancia de Bcrypt para el cifrado de contraseñas
jwt = JWTManager()  # Instancia de JWTManager para la gestión de tokens JWT

# Definición de un formateador de registro personalizado
class RequestFormatter(logging.Formatter):
    def format(self, record):
        if has_request_context():  # Verifica si hay un contexto de solicitud activo
            record.url = request.url  # Agrega la URL de la solicitud al registro
            record.remote_addr = request.remote_addr  # Agrega la dirección IP remota al registro
        else:  # Si no hay contexto de solicitud
            record.url = None  # Establece la URL del registro como None
            record.remote_addr = None  # Establece la dirección IP remota del registro como None

        return super().format(record)  # Llama al método format() de la clase base

# Configuración del controlador de registro para escribir registros en un archivo
handler = logging.FileHandler("app.log")  # Creación de un controlador de archivo
handler.setLevel(logging.NOTSET)  # Establecimiento del nivel de registro
formatter = RequestFormatter(  # Creación de un formateador de registro personalizado
    "[%(asctime)s] %(remote_addr)s requested %(url)s\n%(levelname)s in %(module)s: %(message)s"
)
handler.setFormatter(formatter)  # Establecimiento del formateador en el controlador

logger_app = logging.getLogger(__name__)  # Creación de un objeto de registro
"""Objeto de registro para la aplicación."""

logger_app.addHandler(handler)  # Agrega el controlador al objeto de registro
