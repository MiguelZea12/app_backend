from flask import Blueprint, request
from flask_restx import Api, Resource, Namespace
from marshmallow import ValidationError
from app.utils.response import create_response
from app.services import team_service

team_blueprint = Blueprint("team", __name__, url_prefix="/teams")
team_ns = Namespace("team", description="Team operations")

api = Api(team_blueprint)
api.add_namespace(team_ns)

@team_ns.route("/")
class TeamList(Resource):
    def get(self):
        """Obtener todos los equipos"""
        try:
            teams = team_service.get_all_teams()
            return create_response("success", data={"teams": teams}, status_code=200)
        except Exception as e:
            return create_response("error", message=str(e), status_code=500)

    def post(self):
        """Crear un nuevo equipo"""
        try:
            json_data = request.get_json(force=True)
            name_team = json_data.get("name_team")
            work_group_id = json_data.get("work_group_id")

            new_team = team_service.create_team(name_team, work_group_id)
            return create_response("success", data={"team": new_team}, status_code=201)
        except ValidationError as ve:
            return create_response("error", message=str(ve), status_code=400)
        except Exception as e:
            return create_response("error", message=str(e), status_code=500)
