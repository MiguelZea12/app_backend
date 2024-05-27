from app.extensions import db  
from app.models.declarative_base import DeclarativeBase  
from sqlalchemy.dialects.postgresql import JSONB  
from datetime import datetime

class User(DeclarativeBase):  # Define una nueva clase llamada User que hereda de DeclarativeBase
    __tablename__ = "user"  # Nombre de la tabla en la base de datos
    id = db.Column(db.Integer, primary_key=True)  # Define una columna llamada "id" de tipo Integer y clave primaria
    identification = db.Column(db.String(10), nullable=False)  # Define una columna llamada "identification" de tipo String con una longitud máxima de 15 caracteres y no nula
    name = db.Column(db.String(100), nullable=False)  # Define una columna llamada "username" de tipo String con una longitud máxima de 100 caracteres y no nula
    lastname = db.Column(db.String(100), nullable=False)  # Define una columna llamada "lastname" de tipo String con una longitud máxima de 100 caracteres y no nula
    password = db.Column(db.String(100), nullable=False)  # Define una columna llamada "password" de tipo String con una longitud máxima de 100 caracteres y no nula
    status = db.Column(db.Boolean, nullable=False, default=True)  # Define una columna llamada "status" de tipo Booleano que no puede ser nula y tiene un valor predeterminado de True
    created_at = db.Column(db.DateTime, nullable=False)  # Define una columna llamada "created_at" de tipo DateTime que no puede ser nula
    
    def __init__(self, identification, name, password, lastname, status, created_at):  # Constructor de la clase User
        self.identification = identification  # Asigna el valor de identification al atributo de la instancia
        self.name = name  # Asigna el valor de name al atributo de la instancia
        self.password = password  # Asigna el valor de password al atributo de la instancia
        self.lastname = lastname  # Asigna el valor de lastname al atributo de la instancia
        self.status = status  # Asigna el valor de status al atributo de la instancia
        self.created_at = datetime.now()
