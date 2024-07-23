from app.extensions import db
from sqlalchemy.dialects.postgresql import JSONB

class Caregiver(db.Model):
    __tablename__ = 'caregivers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    document_id = db.Column(db.String(20), unique=True, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    career = db.Column(db.String(100), nullable=False)
    semester = db.Column(db.String(10), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    is_active = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f'<Caregiver {self.name}>'

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'document_id': self.document_id,
            'gender': self.gender,
            'age': self.age,
            'career': self.career,
            'semester': self.semester,
            'city': self.city,
            'is_active': self.is_active
        }
