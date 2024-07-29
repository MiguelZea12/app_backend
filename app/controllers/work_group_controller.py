from flask import Blueprint, request
from flask_restx import Api, Resource, Namespace
from marshmallow import ValidationError
from app.utils.response import create_response
from app.services import work_group_service

workgroup_blueprint = Blueprint("workgroup", __name__, url_prefix="/workgroup")
workgroup_ns = Namespace("workgroup", description="GroupWork operations")

api = Api(workgroup_blueprint)
api.add_namespace(workgroup_ns)

@workgroup_ns.route("/")
class GroupWorkList(Resource):
    def get(self):
        """Obtener todos los grupos de trabajo"""
        try:
            groupworks = work_group_service.get_all_groupworks()
            return create_response("success", data={"groupworks": groupworks}, status_code=200)
        except Exception as e:
            return create_response("error", message=str(e), status_code=500)

    def post(self):
        """Crear un nuevo grupo de trabajo"""
        try:
            json_data = request.get_json(force=True)
            name = json_data.get("name")

            new_groupwork = work_group_service.create_workgroup(name)
            return create_response("success", data={"groupwork": new_groupwork}, status_code=201)
        except ValidationError as ve:
            return create_response("error", message=str(ve), status_code=400)
        except Exception as e:
            return create_response("error", message=str(e), status_code=500)
