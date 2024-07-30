from app.extensions import db
from app.models.role import Role

class RoleService:
    @staticmethod
    def get_all_roles():
        return db.session.query(Role).all()

    @staticmethod
    def get_role_by_id(role_id):
        return db.session.query(Role).get(role_id)

    @staticmethod
    def create_role(data):
        existing_role = db.session.query(Role).filter_by(name=data['name']).first()
        if existing_role:
            return None, "Role with this name already exists."
        new_role = Role(name=data['name'], description=data.get('description'))
        db.session.add(new_role)
        db.session.commit()
        return new_role, None

    @staticmethod
    def update_role(role, data):
        role.name = data['name']
        role.description = data.get('description')
        db.session.commit()
        return role

    @staticmethod
    def delete_role(role):
        db.session.delete(role)
        db.session.commit()
        return None
