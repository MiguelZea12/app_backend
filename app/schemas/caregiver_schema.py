from marshmallow import Schema, fields

class CaregiverSchema(Schema):
    id = fields.Int(dump_only=True)
    canton = fields.Str(required=True)
    parish = fields.Str(required=True)
    zone_type = fields.Str(required=True)
    address = fields.Str(required=True)
    reference = fields.Str(required=False)
    landline_1 = fields.Str(required=False)
    landline_2 = fields.Str(required=False)
    mobile_1 = fields.Str(required=False)
    mobile_2 = fields.Str(required=False)
    caregiver_document_id = fields.Str(required=True)
    caregiver_last_name = fields.Str(required=True)
    caregiver_first_name = fields.Str(required=True)
    caregiver_gender = fields.Str(required=True)
    relationship = fields.Str(required=True)
    is_active = fields.Bool(dump_only=True)