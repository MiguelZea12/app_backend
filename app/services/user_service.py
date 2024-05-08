from sqlalchemy import text
from app.engines import session_bpm
from app.extensions import db, bcrypt_instance
from app.models.user import User
from app.utils.utilities import timeNowTZ
from app.schemas.user_schema import UserSchema


def get_all():
    user_objects = db.session.query(User).filter(User.status == True).all()
    user_list = UserSchema(many=True).dump(user_objects)
    return user_list

