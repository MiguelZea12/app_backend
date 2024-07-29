from app.extensions import db  
from app.models.declarative_base import DeclarativeBase  
from sqlalchemy.dialects.postgresql import ARRAY  
from sqlalchemy.orm import validates

class Team(DeclarativeBase): 
    __tablename__ = "team" 
    id = db.Column(db.Integer, primary_key=True)
    managers = db.Column(ARRAY(db.Integer), nullable=False)

    def __init__(self, managers):
        self.managers = managers

    # Valida que un equipo tenga exactamente 2 gestores y que sean diferentes
    @validates('managers')
    def validate_managers(self, key, value):
        if len(value) != 2:
            raise ValueError("A team must have exactly 2 managers.")
        if value[0] == value[1]:
            raise ValueError("The two managers must be different.")
        return value