import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.extensions import db
from app.models.patinent import Patinet  # Asegúrate de que la importación sea correcta según la estructura de tu proyecto
from datetime import datetime

# Configura la cadena de conexión de SQLAlchemy a tu base de datos
DATABASE_URI = 'postgresql+psycopg2://postgres:12345678@localhost:5432/backvin4'

# Crea una instancia del motor de SQLAlchemy
engine = create_engine(DATABASE_URI)

# Crea una sesión
Session = sessionmaker(bind=engine)
session = Session()

# Lee el archivo Excel
df = pd.read_excel('cuidadores.xls', engine='xlrd')

# Renombra las columnas para que coincidan con los nombres de los atributos del modelo
df.rename(columns={
    'CÉDULA PERSONA BENEFICIARIA': 'cedula_persona_beneficiaria',
    'APELLIDOS PERSONA BENEFICIARIA': 'apellidos_persona_beneficiaria',
    'NOMBRES PERSONA BENEFICIARIA': 'nombres_persona_beneficiaria',
    'SEXO PERSONA BENEFICIARIA': 'sexo_persona_beneficiaria',
    'FECHA NACIMIENTO PERSONA BENEFICIARIA': 'fecha_nacimiento_persona_beneficiaria',
    'EDAD BENEFICIARIA': 'edad_beneficiaria',
    'TIPO DE BENEFICIARIO': 'tipo_de_beneficiario',
    'TIPO DISCAPACIDAD': 'tipo_discapacidad',
    'PORCENTAJE DISCAPACIDAD': 'porcentaje_discapacidad',
    'ESTADO': 'estado',
    'BARRIO': 'barrio'
}, inplace=True)

# Combina nombres y apellidos en una sola columna
df['nombres_completos_persona_beneficiaria'] = df['nombres_persona_beneficiaria'] + ' ' + df['apellidos_persona_beneficiaria']

# Convierte la columna de fecha a datetime, intentando detectar el formato automáticamente
df['fecha_nacimiento_persona_beneficiaria'] = pd.to_datetime(df['fecha_nacimiento_persona_beneficiaria'], errors='coerce')

# Valida y convierte las columnas a los tipos de datos correctos
df['cedula_persona_beneficiaria'] = df['cedula_persona_beneficiaria'].astype(str)
df['edad_beneficiaria'] = pd.to_numeric(df['edad_beneficiaria'], errors='coerce')
df['porcentaje_discapacidad'] = pd.to_numeric(df['porcentaje_discapacidad'], errors='coerce')

# Filtra filas con datos inválidos
df = df.dropna(subset=[
    'cedula_persona_beneficiaria',
    'nombres_completos_persona_beneficiaria',
    'sexo_persona_beneficiaria',
    'fecha_nacimiento_persona_beneficiaria',
    'edad_beneficiaria',
    'tipo_de_beneficiario',
    'tipo_discapacidad',
    'porcentaje_discapacidad',
    'estado'
])

# Verifica los tipos de datos
print(df.dtypes)

# Añade una comprobación de tipo de datos para asegurarte de que todos los valores sean del tipo correcto
for index, row in df.iterrows():
    if not isinstance(row['porcentaje_discapacidad'], (int, float)):
        print(f"Invalid data type for 'porcentaje_discapacidad' at row {index}: {row['porcentaje_discapacidad']}")
    if not isinstance(row['edad_beneficiaria'], int):
        print(f"Invalid data type for 'edad_beneficiaria' at row {index}: {row['edad_beneficiaria']}")
    if not isinstance(row['cedula_persona_beneficiaria'], str):
        print(f"Invalid data type for 'cedula_persona_beneficiaria' at row {index}: {row['cedula_persona_beneficiaria']}")
    if not isinstance(row['barrio'], str):
        print(f"Invalid data type for 'barrio' at row {index}: {row['barrio']}")

# Inserta los datos en la base de datos
for index, row in df.iterrows():
    try:
        user = Patinet(
            cedula_persona_beneficiaria=row['cedula_persona_beneficiaria'],
            nombres_completos_persona_beneficiaria=row['nombres_completos_persona_beneficiaria'],
            sexo_persona_beneficiaria=row['sexo_persona_beneficiaria'],
            fecha_nacimiento_persona_beneficiaria=row['fecha_nacimiento_persona_beneficiaria'],
            edad_beneficiaria=row['edad_beneficiaria'],
            tipo_de_beneficiario=row['tipo_de_beneficiario'],
            tipo_discapacidad=row['tipo_discapacidad'],
            porcentaje_discapacidad=row['porcentaje_discapacidad'],
            estado=row['estado'],
            status=True
        )
        session.add(user)
    except Exception as e:
        print(f"Error inserting row {index}: {e}")
        print(f"Row data: {row}")

# Confirma las transacciones
session.commit()

# Cierra la sesión
session.close()