import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app import create_app
from app.models.caregiver import Caregiver
from app.extensions import db

# Configuración de la aplicación Flask
app = create_app('development')  # o 'production' según tu entorno

with app.app_context():
    # Lee el archivo XLS
    df = pd.read_excel('cuidadores.xls', engine='xlrd')

    # Limpia los nombres de las columnas eliminando espacios adicionales
    df.columns = df.columns.str.strip()

    # Verifica los nombres de las columnas
    print(df.columns)

    # Renombra las columnas para que coincidan con los campos del modelo Caregiver
    df.rename(columns={
        'CANTÓN': 'canton',
        'PARROQUIA': 'parish',
        'TIPO DE ZONA': 'zone_type',
        'DIRECCIÓN': 'address',
        'REFERENCIA': 'reference',
        'TELÉFONO CONVENCIONAL 1': 'landline_1',
        'TELÉFONO CONVENCIONAL 2': 'landline_2',
        'TELÉFONO CELULAR 1': 'mobile_1',
        'TELÉFONO CELULAR 2': 'mobile_2',
        'CÉDULA PERSONA CUIDADORA': 'caregiver_document_id',
        'APELLIDOS PERSONA CUIDADORA': 'caregiver_last_name',
        'NOMBRES PERSONA CUIDADORA': 'caregiver_first_name',
        'SEXO PERSONA CUIDADORA': 'caregiver_gender',
        'PARENTESCO': 'relationship'
    }, inplace=True)

    # Convierte las columnas que deberían ser cadenas a tipo cadena
    columns_to_string = ['caregiver_document_id', 'caregiver_last_name', 'caregiver_first_name', 'caregiver_gender', 'relationship', 'landline_1', 'landline_2', 'mobile_1', 'mobile_2', 'address', 'reference']
    for col in columns_to_string:
        df[col] = df[col].astype(str)

    # Conecta a la base de datos
    DATABASE_URI = app.config['SQLALCHEMY_DATABASE_URI']
    engine = create_engine(DATABASE_URI)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Itera sobre cada fila del DataFrame y crea un nuevo registro en la tabla caregiver
    for index, row in df.iterrows():
        caregiver = Caregiver(
            canton=row['canton'],
            parish=row['parish'],
            zone_type=row['zone_type'],
            address=row['address'],
            reference=row['reference'] if row['reference'] != 'nan' else None,
            landline_1=row['landline_1'] if row['landline_1'] != 'nan' else None,
            landline_2=row['landline_2'] if row['landline_2'] != 'nan' else None,
            mobile_1=row['mobile_1'] if row['mobile_1'] != 'nan' else None,
            mobile_2=row['mobile_2'] if row['mobile_2'] != 'nan' else None,
            caregiver_document_id=row['caregiver_document_id'],
            caregiver_last_name=row['caregiver_last_name'],
            caregiver_first_name=row['caregiver_first_name'],
            caregiver_gender=row['caregiver_gender'],
            relationship=row['relationship'],
            is_active=True
        )
        session.add(caregiver)

    # Confirma las transacciones
    session.commit()

    # Cierra la sesión
    session.close()
