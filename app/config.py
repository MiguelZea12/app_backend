from os import environ, path
from datetime import timedelta


class config(object):
    """
    Clase base de configuración para la aplicación.
    """
    SECRET_KEY = environ.get("SECRET_KEY")  # Clave secreta para la aplicación Flask
    CORS_HEADERS = "Content-Type"  # Encabezados CORS permitidos
    PROPAGATE_EXCEPTIONS = True  # Propagar excepciones en la aplicación

    #: Configuración de JWT
    JWT_SECRET_KEY = environ.get("SECRET_KEY")  # Clave secreta para JWT
    JWT_ALGORITHM = "RS256"  # Algoritmo de cifrado para JWT
    JWT_PRIVATE_KEY = open("app/static/private_key.pem").read()  # Clave privada para JWT (algoritmo asimétrico)
    JWT_PUBLIC_KEY = open("app/static/public_key.pem").read()  # Clave pública para JWT (algoritmo asimétrico)
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)  # Tiempo de expiración del token de acceso JWT
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(hours=2)  # Tiempo de expiración del token de actualización JWT


class DevelopmentConfig(config):
    """
    Clase de configuración para el entorno de desarrollo.
    """
    DEBUG = True  # Modo de depuración activado
    FLASK_DEBUG = 1  # Nivel de depuración de Flask
    SQLALCHEMY_DATABASE_URI = environ.get("DEV_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = True  # Habilitar el seguimiento de modificaciones de SQLAlchemy


class ProductionConfig(config):
    """
    Clase de configuración para el entorno de producción.
    """
    DEBUG = False  # Modo de depuración desactivado
    FLASK_DEBUG = 0  # Nivel de depuración de Flask
    SQLALCHEMY_DATABASE_URI = environ.get("PROD_DATABASE_URI")  # URI de la base de datos para el entorno de producción
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Deshabilitar el seguimiento de modificaciones de SQLAlchemy
    SQLALCHEMY_ECHO = False  # No imprimir todas las consultas SQL ejecutadas por SQLAlchemy
