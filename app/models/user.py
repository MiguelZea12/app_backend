from app.extensions import db  
from app.models.declarative_base import DeclarativeBase  
from sqlalchemy.dialects.postgresql import JSONB  

class User(DeclarativeBase):  # Define una nueva clase llamada User que hereda de DeclarativeBase
    __tablename__ = "user"  # Nombre de la tabla en la base de datos
    id = db.Column(db.Integer, primary_key=True)  # Define una columna llamada "id" de tipo Integer y clave primaria
    identification = db.Column(db.String(15), nullable=False)  # Define una columna llamada "identification" de tipo String con una longitud máxima de 15 caracteres y no nula
    username = db.Column(db.String(100), nullable=False)  # Define una columna llamada "username" de tipo String con una longitud máxima de 100 caracteres y no nula
    lastname = db.Column(db.String(100), nullable=False)  # Define una columna llamada "lastname" de tipo String con una longitud máxima de 100 caracteres y no nula
    status = db.Column(db.Boolean, nullable=False, default=True)  # Define una columna llamada "status" de tipo Booleano que no puede ser nula y tiene un valor predeterminado de True
    
    def __init__(self, identification, username, lastname, status):  # Constructor de la clase User
        self.identification = identification  # Asigna el valor de identification al atributo de la instancia
        self.username = username  # Asigna el valor de username al atributo de la instancia
        self.lastname = lastname  # Asigna el valor de lastname al atributo de la instancia
        self.status = status  # Asigna el valor de status al atributo de la instancia
