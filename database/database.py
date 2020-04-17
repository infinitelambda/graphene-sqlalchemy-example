import os
from ast import literal_eval
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

db_name = 'database.database'
db_path = os.path.join(os.path.dirname(__file__), db_name)
db_uri = 'sqlite:///{}'.format(db_path)
engine = create_engine(db_uri, convert_unicode=True, echo=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

from database.models import PlanetModel, PeopleModel


def init_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    with open('database/data/planet.json', 'r') as file:
        data = literal_eval(file.read())
        for record in data:
            planet = PlanetModel(**record)
            db_session.add(planet)
        db_session.commit()

    with open('database/data/people.json', 'r') as file:
        data = literal_eval(file.read())
        for record in data:
            people = PeopleModel(**record)
            db_session.add(people)
        db_session.commit()
