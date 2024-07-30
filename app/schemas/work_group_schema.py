from marshmallow import fields, post_load
from app.schemas.base_schema import BaseSchema
from app.models.work_group import WorkGroup

class WorkGroupSchema(BaseSchema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)

    @post_load
    def make_workgroup(self, data, **kwargs):
        return WorkGroup(**data)

workgroup_schema = WorkGroupSchema()
workgroups_schema = WorkGroupSchema(many=True)
