import os
from . import config
from .models import Person, DBSession
import transaction
from sqlalchemy.orm.exc import NoResultFound

def increment(person_from, person_to):
    with transaction.manager:
        try:
            person_from_obj = DBSession.query(Person).filter_by(name=person_from).one()
        except NoResultFound:
            person_from_obj = Person(person_from)
            DBSession.add(person_from_obj)
        person_from_obj.fucks_given += 1

        if person_to:
            try:
                person_to_obj = DBSession.query(Person).filter_by(name=person_to).one()
            except NoResultFound:
                person_to_obj = Person(person_to)
                DBSession.add(person_to_obj)
            person_to_obj.fucks_taken += 1


def config_init():
    config.DB_URL = os.environ.get("DB_URL", None)
    config.DEBUG = os.environ.get("DEBUG", False)
