from marshmallow import fields
from app.schemas.base_schema import BaseSchema

class AssignmentSchema(BaseSchema):
    id = fields.Int(dump_only=True)
    login_id = fields.Int(required=True)
    team_id = fields.Int(required=True)
    assigned_at = fields.DateTime(dump_only=True)

assignment_schema = AssignmentSchema()
print(assignment_schema)
