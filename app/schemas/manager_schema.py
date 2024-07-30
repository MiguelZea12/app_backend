from marshmallow import fields
from app.schemas.base_schema import BaseSchema

class ManagerSchema(BaseSchema):
    user_id = fields.Int(dump_only=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    identity_document = fields.Str(required=True)
    gender = fields.Str(required=True)
    age = fields.Int(required=True)
    major = fields.Str(required=True)
    semester = fields.Str(required=True)
    city_of_residence = fields.Str(required=True)
    team_id = fields.Int(required=True)
    status = fields.Bool(dump_only=True)

user_schema = ManagerSchema()
print(user_schema)
