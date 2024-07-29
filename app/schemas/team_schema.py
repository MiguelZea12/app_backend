from marshmallow import fields, post_load
from app.schemas.base_schema import BaseSchema
from app.models.team import Team

class TeamSchema(BaseSchema):
    id = fields.Int(dump_only=True)
    name_team = fields.Str(required=True)
    work_group_id = fields.Int(required=True)

    @post_load
    def make_team(self, data, **kwargs):
        return Team(**data)

team_schema = TeamSchema()
teams_schema = TeamSchema(many=True)
