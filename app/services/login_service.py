import traceback
import jwt
import datetime
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError
from app.extensions import db, bcrypt_instance
from app.models.login import Login
from app.schemas.login_schema import LoginSchema
from flask import current_app as app

def get_all():
    try:
        login_objects = db.session.query(Login).filter(Login.status == True).all()
        login_list = LoginSchema(many=True).dump(login_objects)
        return login_list
    except Exception as e:
        traceback.print_exc()
        return None

def exists(identification: str):
    login_objects = (
        db.session.query(Login)
        .filter(Login.identification == identification, Login.status == True)
        .first()
    )
    return login_objects is not None

def create(identification: str, name: str, lastname: str, manager_id: int, password: str = None):
    try:
        if password is None:
            password = identification 
                
        new_login = Login(
            identification=identification,
            name=name,
            lastname=lastname,
            password=bcrypt_instance.generate_password_hash(password).decode("utf8"),
            manager_id=manager_id,
            status=True
        )
        db.session.add(new_login)
        db.session.commit()
        login_list = LoginSchema(exclude=["password"]).dump(new_login)
        return login_list

    except IntegrityError as ie:
        db.session.rollback()
        raise ValidationError("Error de integridad: " + str(ie.orig))

    except ValidationError as ve:
        raise ve

    except Exception as e:
        traceback.print_exc()
        return None

def authenticate(identification: str, password: str):
    try:
        user = db.session.query(Login).filter(Login.identification == identification, Login.status == True).first()
        if user and bcrypt_instance.check_password_hash(user.password, password):
            token = jwt.encode({
                'identification': user.identification,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # Token expira en 1 hora
            }, app.config['JWT_PRIVATE_KEY'], algorithm=app.config['JWT_ALGORITHM'])
            return {'token': token}
        else:
            return None
    except Exception as e:
        traceback.print_exc()
        return None
