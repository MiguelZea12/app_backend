from app.extensions import db, bcrypt_instance
from app.models.login import Login
from app.models.token_block_list import TokenBlockList
from flask_jwt_extended import create_access_token

def login(username: str, password: str):
    login_object = (
        db.session.query(Login)
        .filter(Login.identification == username, Login.status == True)
        .first()
    )
    if login_object is not None:
        if bcrypt_instance.check_password_hash(login_object.password, password):
            login_identity = {"id": login_object.id, "identification": login_object.identification}
            access_token = create_access_token(identity=login_identity)
            return {"access_token": access_token}
        else:
            return None
    else:
        return None

def logout(jti: str):
    token_block_list = TokenBlockList(jti)
    db.session.add(token_block_list)
    db.session.commit()
    return True
