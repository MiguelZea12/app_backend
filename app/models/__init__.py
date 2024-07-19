"""Modelos ORM de la BD"""
from os.path import dirname, basename, isfile, join
import glob

# Utilizando glob.glob() para encontrar todos los archivos .py en el directorio actual
modules = glob.glob(join(dirname(__file__), "*.py"))

# Creación de una lista __all__ que contendrá los nombres de los archivos .py encontrados
__all__ = [
    basename(f)[:-3]  # Obteniendo el nombre de archivo sin la extensión .py
    for f in modules  # Iterando sobre todos los archivos encontrados
    if isfile(f) and not f.endswith('__init__.py')  # Filtrando solo archivos válidos y no __init__.py
]

# Importación explícita de los modelos
from app.models.user import User
from app.models.role import Role

__all__.extend(['User', 'Role'])  # Añadir explícitamente los modelos importados a __all__
