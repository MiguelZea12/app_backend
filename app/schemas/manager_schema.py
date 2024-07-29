from marshmallow import fields
from app.schemas.base_schema import BaseSchema  # Asegúrate de importar correctamente tu BaseSchema

class ManagerSchema(BaseSchema):  # Define una nueva clase llamada UserSchema que hereda de BaseSchema
    user_id = fields.Int(dump_only=True)  # Define un campo llamado "user_id" que se espera que sea un entero (Int) y solo se serializa (dump_only=True)
    first_name = fields.Str(required=True)  # Define un campo llamado "first_name" que se espera que sea una cadena (Str) y es obligatorio (required=True)
    last_name = fields.Str(required=True)  # Define un campo llamado "last_name" que se espera que sea una cadena (Str) y es obligatorio (required=True)
    identity_document = fields.Str(required=True)  # Define un campo llamado "identity_document" que se espera que sea una cadena (Str) y es obligatorio (required=True)
    gender = fields.Str(required=True)  # Define un campo llamado "gender" que se espera que sea una cadena (Str) y es obligatorio (required=True)
    age = fields.Int(required=True)  # Define un campo llamado "age" que se espera que sea un entero (Int) y es obligatorio (required=True)
    major = fields.Str(required=True)  # Define un campo llamado "major" que se espera que sea una cadena (Str) y es obligatorio (required=True)
    semester = fields.Str(required=True)  # Define un campo llamado "semester" que se espera que sea una cadena (Str) y es obligatorio (required=True)
    city_of_residence = fields.Str(required=True)  # Define un campo llamado "city_of_residence" que se espera que sea una cadena (Str) y es obligatorio (required=True)
    team_id = fields.Int(required=True) # Define un campo llamado "team_id" que se espera que sea un entero (Int) y es obligatorio (required=True)
    status = fields.Bool(dump_only=True)

user_schema = ManagerSchema()
print(user_schema)  # Verificar esquema de serialización
