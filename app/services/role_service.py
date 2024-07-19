from app.extensions import db
from app.models.role import Role


class RoleService:
    @staticmethod
    def get_all_roles():
        """
        Función para obtener todos los roles.

        Retorna:
        - list: Lista de todos los objetos Role en la base de datos.
        """
        return db.session.query(Role).all()

    @staticmethod
    def get_role_by_id(role_id):
        """
        Función para obtener un rol por su ID.

        Parámetros:
        - role_id (int): ID del rol que se desea obtener.

        Retorna:
        - Role: Objeto Role si se encuentra, o None si no se encuentra.
        """
        return db.session.query(Role).get(role_id)

    @staticmethod
    def create_role(data):
        """
        Función para crear un nuevo rol.

        Parámetros:
        - data (dict): Diccionario con los datos necesarios para crear un nuevo rol.

        Retorna:
        - Role: Objeto Role creado.
        - str: Mensaje de error si el rol ya existe, o None si la creación es exitosa.
        """
        existing_role = db.session.query(Role).filter_by(name=data['name']).first()
        if existing_role:
            return None, "Role with this name already exists."
        new_role = Role(name=data['name'], description=data.get('description'))
        db.session.add(new_role)
        db.session.commit()
        return new_role, None

    @staticmethod
    def update_role(role, data):
        """
        Función para actualizar un rol existente.

        Parámetros:
        - role (Role): Objeto Role que se desea actualizar.
        - data (dict): Diccionario con los datos necesarios para actualizar el rol.

        Retorna:
        - Role: Objeto Role actualizado.
        """
        role.name = data['name']
        role.description = data.get('description')
        db.session.commit()
        return role

    @staticmethod
    def delete_role(role):
        """
        Función para eliminar un rol.

        Parámetros:
        - role (Role): Objeto Role que se desea eliminar.

        Retorna:
        - None
        """
        db.session.delete(role)
        db.session.commit()
        return None
