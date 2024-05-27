from os import path
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))

from app import app
if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0')
