import traceback
from sqlalchemy.exc import IntegrityError
from app.extensions import db
from app.models.work_group import WorkGroup
from app.schemas.work_group_schema import workgroup_schema
from marshmallow import ValidationError

def get_all_workgroups():
    try:
        workgroup_objects = db.session.query(WorkGroup).all()
        workgroup_list = workgroup_schema.dump(workgroup_objects, many=True)
        return workgroup_list
    except Exception as e:
        print(f"Error al obtener grupos de trabajo: {str(e)}")
        traceback.print_exc()
        return None

def create_workgroup(name):
    try:
        new_workgroup = WorkGroup(name=name)
        db.session.add(new_workgroup)
        db.session.commit()
        return workgroup_schema.dump(new_workgroup)
    except (ValidationError, ValueError) as ve:
        raise ve
    except IntegrityError as ie:
        db.session.rollback()
        raise ValidationError("Database error: " + str(ie.orig))
    except Exception as e:
        db.session.rollback()
        print(f"Error al crear grupo de trabajo: {str(e)}")
        traceback.print_exc()
        raise e
