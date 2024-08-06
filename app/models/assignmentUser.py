from app.extensions import db
from datetime import datetime
from app.models.declarative_base import DeclarativeBase

class AssignmentUser(DeclarativeBase):
    __tablename__ = 'assignment_users'
    id = db.Column(db.Integer, primary_key=True)
    id_login = db.Column(db.Integer, primary_key=True)
    id_team = db.Column(db.Integer, db.ForeignKey('login.id'), nullable=False)
    assigned_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, id_login, id_team, assigned_at):
        self.id_login = id_login
        self.id_team = id_team
        self.assigned_at = datetime.now()