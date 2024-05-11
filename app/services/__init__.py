"""Servicios de la aplicación."""
from os.path import dirname, basename, isfile, join
import glob
modules = glob.glob(join(dirname(__file__), "*.py"))  # Encuentra todos los archivos .py en el mismo directorio que este archivo
# Crea una lista __all__ que contiene los nombres de todos los archivos .py encontrados, excluyendo __init__.py
__all__ = [basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]