from marshmallow import fields
from app.schemas.base_schema import BaseSchema  # Asegúrate de importar correctamente tu BaseSchema

class UserSchema(BaseSchema):  # Define una nueva clase llamada UserSchema que hereda de BaseSchema
    user_id = fields.Int(dump_only=True)  # Define un campo llamado "user_id" que se espera que sea un entero (Int) y solo se serializa (dump_only=True)
    identification = fields.Str(required=True)  # Define un campo llamado "identification" que se espera que sea una cadena (Str) y es obligatorio (required=True)
    username = fields.Str(required=True)  # Define un campo llamado "username" que se espera que sea una cadena (Str) y es obligatorio (required=True)
    lastname = fields.Str(required=True)  # Define un campo llamado "lastname" que se espera que sea una cadena (Str) y es obligatorio (required=True)
    status = fields.Bool(dump_only=True)  # Define un campo llamado "status" que se espera que sea un booleano (Bool) y solo se serializa (dump_only=True)

user_schema = UserSchema()
print(user_schema)  # Verificar esquema de serialización