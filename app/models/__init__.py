"""Modelos ORM de la BD"""  # Comentario que indica el propósito del código que sigue a continuación
# Importación de funciones específicas del módulo os.path
from os.path import dirname, basename, isfile, join
# Importación del módulo glob para búsqueda de archivos
import glob
# Utilizando glob.glob() para encontrar todos los archivos .py en el directorio actual
modules = glob.glob(join(dirname(__file__), "*.py"))
# Creación de una lista __all__ que contendrá los nombres de los archivos .py encontrados
__all__ = [
    basename(f)[:-3]  # Obteniendo el nombre de archivo sin la extensión .py
    for f in modules  # Iterando sobre todos los archivos encontrados
    if isfile(f) and not f.endswith('__init__.py')  # Filtrando solo archivos válidos y no __init__.py
]
