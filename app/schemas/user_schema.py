from marshmallow import fields
from app.schemas.base_schema import BaseSchema  # Asegúrate de importar correctamente tu BaseSchema

class UserSchema(BaseSchema):
    user_id = fields.Int(dump_only=True)
    identification = fields.Str(required=True)
    username = fields.Str(required=True)
    lastname = fields.Str(required=True)
    status = fields.Bool(dump_only=True)
    
    