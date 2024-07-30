from app.extensions import db
from app.models.declarative_base import DeclarativeBase
from datetime import datetime

class Patinet(DeclarativeBase):  # Cambiar el nombre de la clase a Paciente si es necesario
    __tablename__ = "users"  # Asegúrate de que el nombre de la tabla no entre en conflicto con otras tablas
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cedula_persona_beneficiaria = db.Column(db.String(20), nullable=False, unique=True)
    nombres_completos_persona_beneficiaria = db.Column(db.String(255), nullable=True)
    sexo_persona_beneficiaria = db.Column(db.String(10), nullable=True)
    fecha_nacimiento_persona_beneficiaria = db.Column(db.Date, nullable=True)
    edad_beneficiaria = db.Column(db.String(40), nullable=True)
    tipo_de_beneficiario = db.Column(db.String(50), nullable=True)
    tipo_discapacidad = db.Column(db.String(40), nullable=True)
    porcentaje_discapacidad = db.Column(db.Float, nullable=True)
    estado = db.Column(db.String(50), nullable=True)
    status = db.Column(db.Boolean, nullable=True, default=True)
    created_at = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)

    def __init__(self, cedula_persona_beneficiaria, nombres_completos_persona_beneficiaria, sexo_persona_beneficiaria, fecha_nacimiento_persona_beneficiaria, edad_beneficiaria, tipo_de_beneficiario, tipo_discapacidad, porcentaje_discapacidad, estado, status=True):
        self.cedula_persona_beneficiaria = cedula_persona_beneficiaria
        self.nombres_completos_persona_beneficiaria = nombres_completos_persona_beneficiaria
        self.sexo_persona_beneficiaria = sexo_persona_beneficiaria
        self.fecha_nacimiento_persona_beneficiaria = fecha_nacimiento_persona_beneficiaria
        self.edad_beneficiaria = edad_beneficiaria
        self.tipo_de_beneficiario = tipo_de_beneficiario
        self.tipo_discapacidad = tipo_discapacidad
        self.porcentaje_discapacidad = porcentaje_discapacidad
        self.estado = estado
        self.status = status