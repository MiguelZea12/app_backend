from marshmallow import Schema, fields

class PatinentSchema(Schema):
    id = fields.Int(dump_only=True)
    cedula_persona_beneficiaria = fields.Str(required=True)
    nombres_completos_persona_beneficiaria = fields.Str(required=True)
    sexo_persona_beneficiaria = fields.Str(required=True)
    fecha_nacimiento_persona_beneficiaria = fields.Date(required=True)
    edad_beneficiaria = fields.Int(required=True)
    tipo_de_beneficiario = fields.Str(required=True)
    tipo_discapacidad = fields.Str(required=True)
    porcentaje_discapacidad = fields.Float(required=True)
    estado = fields.Str(required=True)
    status = fields.Bool(dump_only=True)
    created_at = fields.DateTime(dump_only=True)

patinent_schema = PatinentSchema()
patinent_schema = PatinentSchema(many=True)