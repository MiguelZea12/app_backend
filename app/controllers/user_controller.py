from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt
from app.utils.response import create_response
from app.services import user_service

user_blueprint = Blueprint("User", __name__, url_prefix="/user")

@user_blueprint.route("/", methods=["GET"])
#@jwt_required()
def get_all():
    users = user_service.get_all()
    return create_response("success", data={"users": users}, status_code=200)
