from marshmallow import fields, post_load, validates_schema, ValidationError
from app.schemas.base_schema import BaseSchema  
from app.models.team import Team

class TeamSchema(BaseSchema):  
    id = fields.Int(dump_only=True)
    managers = fields.List(fields.Int(), required=True)

    # A la hora de serializar, se devuelve un diccionario con los campos del objeto
    @post_load
    def make_team(self, data, **kwargs):
        return Team(**data)

team_schema = TeamSchema()
