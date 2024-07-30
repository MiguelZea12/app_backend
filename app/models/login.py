from app.extensions import db
from app.models.declarative_base import DeclarativeBase
from sqlalchemy.dialects.postgresql import JSONB
from datetime import datetime

class Login(DeclarativeBase):
    __tablename__ = "login"
    id = db.Column(db.Integer, primary_key=True)
    identification = db.Column(db.String(10), nullable=False, unique=True)
    name = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    status = db.Column(db.Boolean, nullable=False, default=True)
    manager_id = db.Column(db.Integer, db.ForeignKey('manager.id'), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    manager = db.relationship('Manager', backref=db.backref('logins', lazy=True))

    def __init__(self, identification, name, password, lastname, status, manager_id):
        self.identification = identification
        self.name = name
        self.password = password
        self.lastname = lastname
        self.status = status
        self.manager_id = manager_id
        self.created_at = datetime.now()
