from marshmallow import Schema, fields
from app.schemas.base_schema import BaseSchema

class CaregiverSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    document_id = fields.Str(required=True)
    gender = fields.Str(required=True)
    age = fields.Int(required=True)
    career = fields.Str(required=True)
    semester = fields.Str(required=True)
    city = fields.Str(required=True)
    is_active = fields.Bool(dump_only=True)
