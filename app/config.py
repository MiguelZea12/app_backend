from os import environ, path
from datetime import timedelta

class Config(object):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:12345678@localhost:5432/backvin4'
    SECRET_KEY = environ.get("SECRET_KEY")  # Clave secreta para la aplicación Flask
    CORS_HEADERS = "Content-Type"  # Encabezados CORS permitidos
    PROPAGATE_EXCEPTIONS = True  # Propagar excepciones en la aplicación
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Deshabilitar el seguimiento de modificaciones de SQLAlchemy

    #: Configuración de JWT
    JWT_SECRET_KEY = environ.get("SECRET_KEY")  # Clave secreta para JWT
    JWT_ALGORITHM = environ.get("JWT_ALGORITHM", "HS256")  # Algoritmo de cifrado para JWT
    JWT_PRIVATE_KEY = open("app/static/private_key.pem").read()  # Clave privada para JWT (algoritmo asimétrico)
    JWT_PUBLIC_KEY = open("app/static/public_key.pem").read()  # Clave pública para JWT (algoritmo asimétrico)
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)  # Tiempo de expiración del token de acceso JWT
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(hours=2)  # Tiempo de expiración del token de actualización JWT

class DevelopmentConfig(Config):
    DEBUG = True  # Modo de depuración activado
    FLASK_DEBUG = 1  # Nivel de depuración de Flask
    SQLALCHEMY_DATABASE_URI = environ.get("DEV_DATABASE_URI", Config.SQLALCHEMY_DATABASE_URI)  # URI de la base de datos para el entorno de desarrollo

class ProductionConfig(Config):
    DEBUG = False  # Modo de depuración desactivado
    FLASK_DEBUG = 0  # Nivel de depuración de Flask
    SQLALCHEMY_DATABASE_URI = environ.get("PROD_DATABASE_URI", Config.SQLALCHEMY_DATABASE_URI)  # URI de la base de datos para el entorno de producción
    SQLALCHEMY_ECHO = False  # No imprimir todas las consultas SQL ejecutadas por SQLAlchemy
