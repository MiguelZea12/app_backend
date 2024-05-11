from marshmallow import fields
from app.schemas.base_schema import BaseSchema


class AuthSchema(BaseSchema):  # Define una nueva clase llamada AuthSchema que hereda de BaseSchema
    username = fields.Str(required=True)  # Define un campo llamado "username" que se espera que sea una cadena (String) y es obligatorio (required=True)
    password = fields.Str(required=True)  # Define un campo llamado "password" que se espera que sea una cadena (String) y es obligatorio (required=True)
