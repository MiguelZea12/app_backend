from app.extensions import db
from app.models.declarative_base import DeclarativeBase
from datetime import datetime

class User(DeclarativeBase):  # Cambiar el nombre de la clase a Paciente si es necesario
    __tablename__ = "users"  # Asegúrate de que el nombre de la tabla no entre en conflicto con otras tablas
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    canton = db.Column(db.String(100), nullable=False)
    parroquia = db.Column(db.String(100), nullable=False)
    tipo_de_zona = db.Column(db.String(50), nullable=False)
    direccion = db.Column(db.String(255), nullable=False)
    referencia = db.Column(db.String(255), nullable=False)
    telefono_convencional = db.Column(db.String(20), nullable=True)
    telefono_celular = db.Column(db.String(20), nullable=True)
    cedula_persona_cuidadora = db.Column(db.String(20), nullable=False, unique=True)
    nombres_completos_persona_cuidadora = db.Column(db.String(255), nullable=False)
    sexo_persona_cuidadora = db.Column(db.String(10), nullable=False)
    parentesco = db.Column(db.String(50), nullable=False)
    cedula_persona_beneficiaria = db.Column(db.String(20), nullable=False, unique=True)
    nombres_completos_persona_beneficiaria = db.Column(db.String(255), nullable=False)
    sexo_persona_beneficiaria = db.Column(db.String(10), nullable=False)
    fecha_nacimiento_persona_beneficiaria = db.Column(db.Date, nullable=False)
    edad_beneficiaria = db.Column(db.Integer, nullable=False)
    tipo_de_beneficiario = db.Column(db.String(50), nullable=False)
    tipo_discapacidad = db.Column(db.String(50), nullable=False)
    porcentaje_discapacidad = db.Column(db.Float, nullable=False)
    estado = db.Column(db.String(50), nullable=False)
    barrio = db.Column(db.String(100), nullable=False)
    status = db.Column(db.Boolean, nullable=False, default=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, canton, parroquia, tipo_de_zona, direccion, referencia, telefono_convencional, telefono_celular, cedula_persona_cuidadora, nombres_completos_persona_cuidadora, sexo_persona_cuidadora, parentesco, cedula_persona_beneficiaria, nombres_completos_persona_beneficiaria, sexo_persona_beneficiaria, fecha_nacimiento_persona_beneficiaria, edad_beneficiaria, tipo_de_beneficiario, tipo_discapacidad, porcentaje_discapacidad, estado, barrio, status=True):
        self.canton = canton
        self.parroquia = parroquia
        self.tipo_de_zona = tipo_de_zona
        self.direccion = direccion
        self.referencia = referencia
        self.telefono_convencional = telefono_convencional
        self.telefono_celular = telefono_celular
        self.cedula_persona_cuidadora = cedula_persona_cuidadora
        self.nombres_completos_persona_cuidadora = nombres_completos_persona_cuidadora
        self.sexo_persona_cuidadora = sexo_persona_cuidadora
        self.parentesco = parentesco
        self.cedula_persona_beneficiaria = cedula_persona_beneficiaria
        self.nombres_completos_persona_beneficiaria = nombres_completos_persona_beneficiaria
        self.sexo_persona_beneficiaria = sexo_persona_beneficiaria
        self.fecha_nacimiento_persona_beneficiaria = fecha_nacimiento_persona_beneficiaria
        self.edad_beneficiaria = edad_beneficiaria
        self.tipo_de_beneficiario = tipo_de_beneficiario
        self.tipo_discapacidad = tipo_discapacidad
        self.porcentaje_discapacidad = porcentaje_discapacidad
        self.estado = estado
        self.barrio = barrio
        self.status = status
