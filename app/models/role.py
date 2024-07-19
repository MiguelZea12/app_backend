from app.extensions import db
from app.models.declarative_base import DeclarativeBase

class Role(DeclarativeBase):  # Define una nueva clase llamada Role que hereda de DeclarativeBase
    __tablename__ = "roles"  # Nombre de la tabla en la base de datos
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # Define una columna llamada "id" de tipo Integer, clave primaria y autoincremental
    name = db.Column(db.String(50), nullable=False, unique=True)  # Define una columna llamada "name" de tipo String con una longitud máxima de 50 caracteres, no nula y única
    description = db.Column(db.String(200), nullable=True)  # Define una columna llamada "description" de tipo String con una longitud máxima de 200 caracteres y puede ser nula

    def __init__(self, name, description=None):  # Constructor de la clase Role
        self.name = name  # Asigna el valor de name al atributo de la instancia
        self.description = description  # Asigna el valor de description al atributo de la instancia

    def to_dict(self):  # Método para convertir el objeto a un diccionario
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }
