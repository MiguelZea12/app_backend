from app.extensions import db
from app.models.declarative_base import DeclarativeBase

class Team(DeclarativeBase):
    __tablename__ = 'team'
    id = db.Column(db.Integer, primary_key=True)
    name_team = db.Column(db.String, nullable=False)
    work_group_id = db.Column(db.Integer, db.ForeignKey('work_group.id'), nullable=False)

    def __init__(self, name_team, work_group_id):
        self.name_team = name_team
        self.work_group_id = work_group_id
