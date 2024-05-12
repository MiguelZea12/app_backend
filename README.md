# Resumen
## Backend del proyecto de vinculacion
La Plataforma de Gestión Médica es una aplicación diseñada para proporcionar atención médica efectiva y especializada a personas con capacidad dependiente, que requieren asistencia médica regular. Este sistema informático administrativo permite generar un seguimiento completo de la atención médica, enfermería y cuidado médico, con el objetivo de convertir cualquier ubicación en una unidad de salud completamente funcional. Con una base de datos de usuarios integral, gestores de seguimiento médico y enfermería, la plataforma facilita la valoración inicial de pacientes, el seguimiento médico continuo, la atención a domicilio y la planificación de tratamientos personalizados.

Backend realizado con las siguientes tecnologias:

### Lenguaje de programacion:
- Python version 3.9
### Framework:
- Flask 
### Base de datos:
- Postgresql 14
### Librerias:
- Flask
- Werkzeug
- requests
- flask-restx
- flask-bcrypt
- flask-sqlalchemy
- flask-cors
- marshmallow
- bcrypt
- psycopg2
- python-dotenv
- pylint
- MarkupSafe
- sentry_sdk
- flask_jwt_extended



## Instalacion y Inicializacion

#### 1. Clona este repositorio en tu máquina local:

```bash
  git clone https://github.com/MiguelZea12/app_backend.git
```

#### 2. Inicia el contenedor Docker:

```bash
docker-compose up -d
```

#### 2.1 Ver si los contenedores estan funcionando.
```bash
docker ps
```
#### 2.2. Detener docker.
```bash
docker-compose down
```
#### 2.3. Resetear el docker.
```bash
docker restart
```


## Interfaz

```bash
app_backend-web-1  |  * Running on all addresses (0.0.0.0)
app_backend-web-1  |  * Running on http://127.0.0.1:5000
app_backend-web-1  |  * Running on http://172.29.0.3:5000
```

## Utilizar pylint

#### 1. Ejecuta Pylint en el directorio del proyecto:

```bash
pylint <nombre_del_directorio>
```

```bash
pylint app
```

## Utilizar Swagger

#### 1. En la url colocal el:
 ```bash
 http://127.0.0.1:5000/<nombre del blueprint>
```

```bash
http://127.0.0.1:5000/user/
```
## Autores

- [@Alejandro Zea](https://github.com/MiguelZea12)
- [@Jose Teran](https://github.com/nightydev)
- [@Julio Vinces](https://github.com/Julius266)
- [@Byron Serrano](https://github.com/ByronSerrano)
- [@Juan Daza](https://github.com/Dazaiyan)
- [@Chistian Encalada](https://github.com/Christian-Encalada)
- [@Aldair Toala](https://github.com/Aldair2003)
- [@Eddie Ajoy]()



# Abstract
## Backend of the linkage project

The Medical Management Platform is an application designed to provide effective and specialized medical care to people with dependent capacity who require regular medical assistance. This administrative computer system allows for comprehensive tracking of medical care, nursing, and medical assistance, with the aim of turning any location into a fully functional health unit. With a comprehensive user database, medical and nursing tracking managers, the platform facilitates initial patient assessment, continuous medical monitoring, home care, and personalized treatment planning.

Backend implemented with the following technologies:

### Programming Language:
- Python version 3.9
### Framework:
- Flask
### Database:
- Postgresql 14
### Libraries:
- Flask
- Werkzeug
- requests
- flask-restx
- flask-bcrypt
- flask-sqlalchemy
- flask-cors
- marshmallow
- bcrypt
- psycopg2
- python-dotenv
- pylint
- MarkupSafe
- sentry_sdk
- flask_jwt_extended

## Installation and Initialization

#### 1. Clone this repository to your local machine:

```bash
  git clone https://github.com/MiguelZea12/app_backend.git
```
#### 2. Start the Docker container:
```bash
docker-compose up -d
```
#### 2.1. Check if the containers are running.
```bash
docker ps
```
#### 2.2. Stop Docker.
```bash
docker-compose down
```
#### 2.3. Reset Docker.
```bash
docker restart
```
## Interface

```bash
app_backend-web-1  |  * Running on all addresses (0.0.0.0)
app_backend-web-1  |  * Running on http://127.0.0.1:5000
app_backend-web-1  |  * Running on http://172.29.0.3:5000
```
## Using pylint
#### 1. Execute Pylint in the project directory:
```bash
pylint <nombre_del_directorio>
```

```bash
pylint app
```

## Using Swagger
#### 1. In the URL, place the following:
```bash
http://127.0.0.1:5000/<blueprint_name>
```

```bash
http://127.0.0.1:5000/user/
```

## Authors
- [@Alejandro Zea](https://github.com/MiguelZea12)
- [@Jose Teran](https://github.com/nightydev)
- [@Julio Vinces](https://github.com/Julius266)
- [@Byron Serrano](https://github.com/ByronSerrano)
- [@Juan Daza](https://github.com/Dazaiyan)
- [@Chistian Encalada](https://github.com/Christian-Encalada)
- [@Aldair Toala](https://github.com/Aldair2003)
- [@Eddie Ajoy]()