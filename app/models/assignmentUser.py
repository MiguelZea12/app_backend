from marshmallow import fields
from app.schemas.base_schema import BaseSchema

class AssignmentUserSchema(BaseSchema):
    id = fields.Int(dump_only=True)
    login_id = fields.Int(required=True)
    team_id = fields.Int(required=True)
    assigned_at = fields.DateTime(dump_only=True)

assignment_user_schema = AssignmentUserSchema()
