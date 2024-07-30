from flask import Blueprint
from os.path import dirname, basename, isfile, join
import os
import glob
import importlib.util
<<<<<<< HEAD
from app.controllers.user_controller import user_ns  # Importa el Namespace aquí
from app.controllers.caregiver_controller import caregiver_ns  # Importa el Namespace aquí
=======
from app.controllers.login_controller import login_ns  # Importa el Namespace aquí
>>>>>>> 296ef3f52140a6cac820928891a12b339a941efb

modules = glob.glob(join(dirname(__file__), "*.py"))
__all__ = [basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]

# Obtener la lista de archivos en el módulo 'controllers'
controllers_dir = os.path.dirname(__file__)
module_files = [f for f in os.listdir(controllers_dir) if f.endswith('.py') and f != '__init__.py']

# Crear una lista para almacenar las instancias de Blueprints
__blueprints__ = []

# Importar y buscar instancias de Blueprints en cada archivo
for module_file in module_files:
    module_name = os.path.splitext(module_file)[0]
    module_path = os.path.join(controllers_dir, module_file)

    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    for name in dir(module):
        item = getattr(module, name)
        if isinstance(item, Blueprint) and name.endswith("_blueprint"):
            __blueprints__.append(item)

# Agrega el Namespace a __all__
<<<<<<< HEAD
__all__.append("user_ns")
__all__.append("caregiver_ns")

# Define la función register_namespaces
def register_namespaces(api):
    api.add_namespace(user_ns)
    api.add_namespace(caregiver_ns)  # Registra el namespace de caregiver
=======
__all__.append("login_ns")

# Define la función register_namespaces
def register_namespaces(api):
    api.add_namespace(login_ns)
>>>>>>> 296ef3f52140a6cac820928891a12b339a941efb
    # Puedes agregar otros namespaces aquí
