from marshmallow import fields, validates, ValidationError
from app.schemas.base_schema import BaseSchema
from app.models.login import Login
from app.extensions import db

class LoginSchema(BaseSchema):
    login_id = fields.Int(dump_only=True)
    identification = fields.Str(required=True)
    name = fields.Str(required=True)
    password = fields.Str(required=True)
    lastname = fields.Str(required=True)
    status = fields.Bool(dump_only=True)
    manager_id = fields.Int(required=True)
    created_at = fields.DateTime(dump_only=True, format='%Y-%m-%d %H:%M:%S%z')

    @validates('identification')
    def validate_identification(self, value):
        if db.session.query(Login).filter_by(identification=value).first():
            raise ValidationError('Identification must be unique.')

login_schema = LoginSchema()
print(login_schema)
