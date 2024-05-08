from app.extensions import db
from app.models.declarative_base import DeclarativeBase
from sqlalchemy.dialects.postgresql import JSONB

class User(DeclarativeBase):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    identification = db.Column(db.String(15), nullable=False)
    username = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    status = db.Column(db.Boolean, nullable=False, default=True)
    