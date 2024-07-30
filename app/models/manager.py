from app.extensions import db
from app.models.declarative_base import DeclarativeBase

class Manager(DeclarativeBase):
    __tablename__ = 'manager'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=True)
    last_name = db.Column(db.String(100), nullable=True)
    identity_document = db.Column(db.String(50), unique=True, nullable=True)
    gender = db.Column(db.String(10), nullable=True)
    age = db.Column(db.Integer, nullable=True)
    major = db.Column(db.String(100), nullable=True)
    semester = db.Column(db.String(50), nullable=True)
    city_of_residence = db.Column(db.String(100), nullable=True)
    status = db.Column(db.Boolean, nullable=True, default=True)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=True)

    def __init__(self, first_name, last_name, identity_document, gender, age, major, semester, city_of_residence, status, team_id):
        self.first_name = first_name
        self.last_name = last_name
        self.identity_document = identity_document
        self.gender = gender
        self.age = age
        self.major = major
        self.semester = semester
        self.city_of_residence = city_of_residence
        self.team_id = team_id
        self.status = status
