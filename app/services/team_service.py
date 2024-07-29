import traceback
from sqlalchemy.exc import IntegrityError
from app.extensions import db
from app.models.team import Team
from app.models.manager import Manager 
from app.schemas.team_schema import team_schema
from marshmallow import ValidationError

def get_all_teams():
    try:
        team_objects = db.session.query(Team).all()
        team_list = team_schema.dump(team_objects, many=True)
        return team_list
    except Exception as e:
        print(f"Error al obtener equipos: {str(e)}")
        traceback.print_exc()
        return None

def create_team(managers):
    try:
        # Verifica que los IDs de los gestores existen en la base de datos
        manager_1 = db.session.query(Manager).get(managers[0])
        manager_2 = db.session.query(Manager).get(managers[1])
        if not manager_1 or not manager_2:
            raise ValidationError("Both manager IDs must exist in the database.")

        new_team = Team(managers=managers)
        db.session.add(new_team)
        db.session.commit()
        return team_schema.dump(new_team)

    except (ValidationError, ValueError) as ve:
        raise ve

    except IntegrityError as ie:
        db.session.rollback()
        raise ValidationError("Database error: " + str(ie.orig))

    except Exception as e:
        db.session.rollback()
        print(f"Error al crear equipo: {str(e)}")
        traceback.print_exc()
        raise e
