"""Instancias de Conexión a Bases de Datos"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

BPM_DATABASE_URI = "mysql+mysqlconnector://usr-procesos:p_gpm_procesos@201.159.223.208:9876/p_gpm_aflow"
engineBPM = create_engine(BPM_DATABASE_URI)
SessionBPM = sessionmaker(bind=engineBPM)
session_bpm = SessionBPM()

# from sqlalchemy import create_engine
# from os import path, environ
# from dotenv import load_dotenv

# basedir = path.abspath(path.dirname(__file__))
# load_dotenv(path.join(basedir, '.env'))


# #: Se crea la conexión a la BD
# db_engine = create_engine(url=environ.get('ADDITIONAL_DATABASE_URI'), pool_size=20, max_overflow=0, pool_recycle=14400, pool_pre_ping=True)
# """DB Engine"""
