from flask import Blueprint, request, jsonify
from flask_restx import Api, Resource, Namespace
from app.services import user_service
from app.schemas.user_schema import user_schema, users_schema

patient_bp = Blueprint("patient_bp", __name__, url_prefix="/patient")
patient_ns = Namespace("patient", description="Patient operations")
api = Api(patient_bp)
api.add_namespace(patient_ns)

@patient_ns.route("/")
class PatientList(Resource):
    def get(self):
        users = user_service.get_all_users()
        return jsonify(users)
    
    def post(self):
        data = request.get_json()
        new_user = user_service.create_user(data)
        return jsonify(new_user), 201

@patient_ns.route("/<int:user_id>")
class PatientDetail(Resource):
    def get(self, user_id):
        user = user_service.get_user_by_id(user_id)
        if user:
            return jsonify(user)
        return jsonify({"message": "User not found"}), 404
    
    def put(self, user_id):
        data = request.get_json()
        updated_user = user_service.update_user(user_id, data)
        if updated_user:
            return jsonify(updated_user)
        return jsonify({"message": "User not found"}), 404

@patient_ns.route("/disable/<int:user_id>")
class PatientDisable(Resource):
    def put(self, user_id):
        disabled_user = user_service.disable_user(user_id)
        if disabled_user:
            return jsonify(disabled_user)
        return jsonify({"message": "User not found"}), 404
