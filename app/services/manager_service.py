import traceback
from sqlalchemy import text
from app.extensions import db
from app.models.manager import Manager
from app.schemas.manager_schema import ManagerSchema

def get_all_managers():
    try:
        manager_objects = db.session.query(Manager).all()
        manager_list = ManagerSchema(many=True).dump(manager_objects)
        return manager_list
    except Exception as e:
        traceback.print_exc()
        return None

def toggle_manager_status(identity_document, new_status):
    try:
        manager = db.session.query(Manager).filter(Manager.identity_document == identity_document).first()
        if not manager:
            return None
        
        manager.status = new_status
        db.session.commit()

        manager_schema = ManagerSchema()
        manager_data = manager_schema.dump(manager)
        return manager_data
    except Exception as e:
        traceback.print_exc()
        return None

def create_manager(data):
    try:
        new_manager_data = ManagerSchema().load(data)
        existing_manager = db.session.query(Manager).filter_by(identity_document=new_manager_data['identity_document']).first()
        if existing_manager:
            return {"error": "El manager con este documento de identidad ya existe."}
        
        new_manager = Manager(
            first_name=new_manager_data['first_name'],
            last_name=new_manager_data['last_name'],
            identity_document=new_manager_data['identity_document'],
            gender=new_manager_data['gender'],
            age=new_manager_data['age'],
            major=new_manager_data['major'],
            semester=new_manager_data['semester'],
            city_of_residence=new_manager_data['city_of_residence'],
            team_id=new_manager_data['team_id'],
            status=True
        )
        
        db.session.add(new_manager)
        db.session.commit()

        manager_data = ManagerSchema().dump(new_manager)
        return manager_data
    except Exception as e:
        traceback.print_exc()
        return {"error": "Ocurrió un error al crear el manager."}
    
def update_manager(manager_id, data):
    try:
        manager = db.session.query(Manager).filter(Manager.id == manager_id).first()
        if not manager:
            return None
        
        manager.first_name = data.get('first_name', manager.first_name)
        manager.last_name = data.get('last_name', manager.last_name)
        manager.identity_document = data.get('identity_document', manager.identity_document)
        manager.gender = data.get('gender', manager.gender)
        manager.age = data.get('age', manager.age)
        manager.major = data.get('major', manager.major)
        manager.semester = data.get('semester', manager.semester)
        manager.city_of_residence = data.get('city_of_residence', manager.city_of_residence)
        
        db.session.commit()

        manager_schema = ManagerSchema()
        manager_data = manager_schema.dump(manager)
        return manager_data
    except Exception as e:
        traceback.print_exc()
        return None

def get_manager_by_identity_document(identity_document):
    try:
        manager = db.session.query(Manager).filter(Manager.identity_document == identity_document).first()
        if not manager:
            return None
        
        manager_schema = ManagerSchema()
        manager_data = manager_schema.dump(manager)
        return manager_data
    except Exception as e:
        traceback.print_exc()
        return None
