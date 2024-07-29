from app.extensions import db
from app.models.declarative_base import DeclarativeBase

class WorkGroup(DeclarativeBase):
    __tablename__ = 'work_group'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    # Relación unidireccional hacia `Teams`
    teams = db.relationship('Team', backref='group_work', lazy=True)

    def __init__(self, name):
        self.name = name
