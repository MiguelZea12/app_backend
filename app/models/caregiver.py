from app.extensions import db
from app.models.declarative_base import DeclarativeBase

class Caregiver(DeclarativeBase):
    __tablename_ = 'caregivers'
    id = db.Column(db.Integer, primary_key=True)
    canton = db.Column(db.String(100), nullable=False)
    parish = db.Column(db.String(100), nullable=False)
    zone_type = db.Column(db.String(50), nullable=False)
    address = db.Column(db.Text, nullable=False)
    reference = db.Column(db.Text, nullable=True)
    landline_1 = db.Column(db.String(20), nullable=True)
    landline_2 = db.Column(db.String(20), nullable=True)
    mobile_1 = db.Column(db.String(20), nullable=True)
    mobile_2 = db.Column(db.String(20), nullable=True)
    caregiver_document_id = db.Column(db.String(20), nullable=False, unique=True)
    caregiver_last_name = db.Column(db.String(100), nullable=False)
    caregiver_first_name = db.Column(db.String(100), nullable=False)
    caregiver_gender = db.Column(db.String(10), nullable=False)
    relationship = db.Column(db.String(50), nullable=False)
    is_active = db.Column(db.Boolean, default=True)

    def _init_(self, canton, parish, zone_type, address, reference, landline_1, landline_2, mobile_1, mobile_2, caregiver_document_id, caregiver_last_name, caregiver_first_name, caregiver_gender, relationship, is_active=True):
        self.canton = canton
        self.parish = parish
        self.zone_type = zone_type
        self.address = address
        self.reference = reference
        self.landline_1 = landline_1
        self.landline_2 = landline_2
        self.mobile_1 = mobile_1
        self.mobile_2 = mobile_2
        self.caregiver_document_id = caregiver_document_id
        self.caregiver_last_name = caregiver_last_name
        self.caregiver_first_name = caregiver_first_name
        self.caregiver_gender = caregiver_gender
        self.relationship = relationship
        self.is_active = is_active

    def _repr_(self):
        return f'<Caregiver {self.caregiver_first_name} {self.caregiver_last_name}>'