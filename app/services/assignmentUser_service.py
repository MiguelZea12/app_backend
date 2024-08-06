import traceback
from sqlalchemy import text
from app.extensions import db
from app.models.assignmentUser import AssignmentUser
from app.schemas.assignmentUser_schema import AssignmentSchema

def get_all_assignments():
    try:
        assignment_objects = db.session.query(AssignmentUser).all()
        assignment_list = AssignmentSchema(many=True).dump(assignment_objects)
        return assignment_list
    except Exception as e:
        traceback.print_exc()
        return None

def get_assignments_by_team_id(team_id):
    try:
        assignments = db.session.query(AssignmentUser).filter(AssignmentUser.team_id == team_id).all()
        if not assignments:
            return None
        
        assignments_schema = AssignmentSchema(many=True)
        assignments_data = assignments_schema.dump(assignments)
        return assignments_data
    except Exception as e:
        traceback.print_exc()
        return None

def create_assignment(data):
    try:
        new_assignment_data = AssignmentSchema().load(data)
        existing_assignment = db.session.query(AssignmentUser).filter_by(login_id=new_assignment_data['login_id']).first()
        if existing_assignment:
            return {"error": "El usuario ya tiene una asignación."}
        
        new_assignment = AssignmentUser(
            login_id=new_assignment_data['login_id'],
            team_id=new_assignment_data['team_id']
        )
        
        db.session.add(new_assignment)
        db.session.commit()

        assignment_data = AssignmentSchema().dump(new_assignment)
        return assignment_data
    except Exception as e:
        traceback.print_exc()
        return {"error": "Ocurrió un error al crear la asignación."}

def update_assignment(assignment_id, data):
    try:
        assignment = db.session.query(AssignmentUser).filter(AssignmentUser.id == assignment_id).first()
        if not assignment:
            return None
        
        assignment.login_id = data.get('login_id', assignment.login_id)
        assignment.team_id = data.get('team_id', assignment.team_id)
        
        db.session.commit()

        assignment_schema = AssignmentSchema()
        assignment_data = assignment_schema.dump(assignment)
        return assignment_data
    except Exception as e:
        traceback.print_exc()
        return None

def delete_assignment(assignment_id):
    try:
        assignment = db.session.query(AssignmentUser).filter(AssignmentUser.id == assignment_id).first()
        if not assignment:
            return None
        
        db.session.delete(assignment)
        db.session.commit()
        return {"message": "Asignación eliminada correctamente"}
    except Exception as e:
        traceback.print_exc()
        return {"error": "Ocurrió un error al eliminar la asignación."}
