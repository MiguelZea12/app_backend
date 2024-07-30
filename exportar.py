import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app import create_app
from app.models.manager import Manager
from app.extensions import db

# Configuración de la aplicación Flask
app = create_app('development')  # o 'production' según tu entorno

with app.app_context():
    # Lee el archivo XLSX
    df = pd.read_excel('gestores.xlsx')

    # Limpia los nombres de las columnas eliminando espacios adicionales
    df.columns = df.columns.str.strip()

    # Verifica los nombres de las columnas
    print(df.columns)

    # Asegúrate de que la columna que contiene los nombres completos se llame 'full_name'
    df.rename(columns={'first_name': 'full_name'}, inplace=True)

    # Función para dividir el nombre completo en nombres y apellidos
    def split_name(full_name):
        parts = full_name.split()
        first_name = parts[-1]
        last_name = ' '.join(parts[:-1])
        return first_name, last_name

    # Aplica la función a cada fila del DataFrame
    df[['first_name', 'last_name']] = df['full_name'].apply(lambda x: pd.Series(split_name(x)))

    # Convierte la columna 'identification_document' a cadena
    df['identification_document'] = df['identification_document'].astype(str)

    # Conecta a la base de datos
    DATABASE_URI = app.config['SQLALCHEMY_DATABASE_URI']
    engine = create_engine(DATABASE_URI)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Itera sobre cada fila del DataFrame y crea un nuevo registro en la tabla manager
    for index, row in df.iterrows():
        manager = Manager(
            first_name=row['first_name'],
            last_name=row['last_name'],
            identity_document=row['identification_document'],
            gender=row['gender'],
            age=row['age'],
            major=row['major'],
            semester=row['semester'],
            city_of_residence=row['city_of_residence'],
            status=True,  # Asignar el estado inicial como True (activo)
            team_id=None  # Asigna el ID del equipo adecuado
        )
        session.add(manager)

    # Confirma las transacciones
    session.commit()

    # Cierra la sesión
    session.close()
