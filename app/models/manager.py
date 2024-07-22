from app.extensions import db  
from app.models.declarative_base import DeclarativeBase  
from sqlalchemy.dialects.postgresql import JSONB  

class Manager(DeclarativeBase):  # Define una nueva clase llamada User que hereda de DeclarativeBase
    __tablename__ = "manager"  # Nombre de la tabla en la base de datos
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    identity_document = db.Column(db.String(50), unique=True, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    major = db.Column(db.String(100), nullable=False)
    semester = db.Column(db.String(50), nullable=False)
    city_of_residence = db.Column(db.String(100), nullable=False)
    status = db.Column(db.Boolean, nullable=False, default=True)  
    

    def __init__(self, first_name, last_name, identity_document, gender, age, major, semester, city_of_residence,status):
        self.first_name = first_name
        self.last_name = last_name
        self.identity_document = identity_document
        self.gender = gender
        self.age = age
        self.major = major
        self.semester = semester
        self.city_of_residence = city_of_residence
        self.status = status
