from marshmallow import fields
from app.schemas.base_schema import BaseSchema  # Asegúrate de importar correctamente tu BaseSchema

class LoginSchema(BaseSchema):  # Define una nueva clase llamada UserSchema que hereda de BaseSchema
    login_id = fields.Int(dump_only=True)  # Define un campo llamado "login_id" que se espera que sea un entero (Int) y solo se serializa (dump_only=True)
    identification = fields.Str(required=True, unique=True)  # Define un campo llamado "identification" que se espera que sea una cadena (Str) y es obligatorio (required=True)
    name = fields.Str(required=True)  # Define un campo llamado "name" que se espera que sea una cadena (Str) y es obligatorio (required=True)
    password = fields.Str(required=True)  # Define un campo llamado "password" que se espera que sea una cadena (Str) y es obligatorio (required=True)
    lastname = fields.Str(required=True)  # Define un campo llamado "lastname" que se espera que sea una cadena (Str) y es obligatorio (required=True)
    status = fields.Bool(dump_only=True)  # Define un campo llamado "status" que se espera que sea un booleano (Bool) y solo se serializa (dump_only=True)
    created_at = fields.DateTime(dump_only=True, format='%Y-%m-%d %H:%M:%S%z')  # Define un campo llamado "created_at" que se espera que sea una fecha y hora (DateTime) y solo se serializa (dump_only=True)
login_schema = LoginSchema()
print(login_schema)  # Verificar esquema de serialización
