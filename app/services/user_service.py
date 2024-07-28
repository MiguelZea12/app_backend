from app.extensions import db
from app.models.user import User
from app.schemas.user_schema import UserSchema, users_schema

def create_user(data):
    user_data = UserSchema().load(data)
    new_user = User(**user_data)
    db.session.add(new_user)
    db.session.commit()
    return UserSchema().dump(new_user)

def get_all_users():
    users = User.query.all()
    return users_schema.dump(users)

def get_user_by_id(user_id):
    user = User.query.get(user_id)
    return UserSchema().dump(user) if user else None

def update_user(user_id, data):
    user = User.query.get(user_id)
    if not user:
        return None
    user_data = UserSchema().load(data, partial=True)
    for key, value in user_data.items():
        setattr(user, key, value)
    db.session.commit()
    return UserSchema().dump(user)

def disable_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return None
    user.status = False
    db.session.commit()
    return UserSchema().dump(user)
