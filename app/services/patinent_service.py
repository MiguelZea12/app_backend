from app.extensions import db
from app.models.patinent import Patinet
from app.schemas.patient_schemas import PatinentSchema

def create_user(data):
    user_data = PatinentSchema().load(data)
    new_user = Patinet(**user_data)
    db.session.add(new_user)
    db.session.commit()
    return PatinentSchema().dump(new_user)

def get_all_users():
    patinent = db.session.query(Patinet).all()
    return PatinentSchema.dump(patinent)

def get_user_by_id(user_id):
    user = Patinet.query.get(user_id)
    return PatinentSchema().dump(user) if user else None

def update_user(user_id, data):
    user = Patinet.query.get(user_id)
    if not user:
        return None
    user_data = PatinentSchema().load(data, partial=True)
    for key, value in user_data.items():
        setattr(user, key, value)
    db.session.commit()
    return PatinentSchema().dump(user)

def disable_user(user_id):
    user = Patinet.query.get(user_id)
    if not user:
        return None
    user.status = False
    db.session.commit()
    return PatinentSchema().dump(user)