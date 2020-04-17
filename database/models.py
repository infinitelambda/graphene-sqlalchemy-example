from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, foreign
from database.database import Base


class PeopleModel(Base):
    # People model

    __tablename__ = 'people'

    id = Column('id', Integer, primary_key=True, doc="Id of the person.")
    name = Column('name', String, doc="Name of the person.")
    height = Column('height', String, doc="Height of the person.")
    mass = Column('mass', String, doc="Mass of the person.")
    hair_color = Column('hair_color', String, doc="Hair color of the person.")
    skin_color = Column('skin_color', String, doc="Skin color of the person.")
    eye_color = Column('eye_color', String, doc="Eye color of the person.")
    birth_year = Column('birth_year', String, doc="Birth year of the person.")
    gender = Column('gender', String, doc="Gender of the person.")
    planet_id = Column('planet_id', Integer, ForeignKey('planet.id'), doc="Id of the home planet of the person.")
    created = Column('created', String, doc="Record created date.")
    edited = Column('edited', String, doc="Record last updated date.")
    url = Column('url', String, doc="URL of the person in the Star Wars API.")


class PlanetModel(Base):
    # Planet model

    __tablename__ = 'planet'

    id = Column('id', Integer, primary_key=True, doc="Id of the person.")
    name = Column('name', String, doc="Name of the planet.")
    rotation_period = Column('rotation_period', String, doc="Rotation period of the planet.")
    orbital_period = Column('orbital_period', String, doc="Orbital period of the planet.")
    diameter = Column('diameter', String, doc="Diameter of the planet.")
    climate = Column('climate', String, doc="Climate period of the planet.")
    gravity = Column('gravity', String, doc="Gravity of the planet.")
    terrain = Column('terrain', String, doc="Terrain of the planet.")
    surface_water = Column('surface_water', String, doc="Surface water of the planet.")
    population = Column('population', String, doc="Population of the planet.")
    created = Column('created', String, doc="Record created date.")
    edited = Column('edited', String, doc="Record last updated date.")
    url = Column('url', String, doc="URL of the planet in the Star Wars API.")

    people_list = relationship(PeopleModel, backref='planet')
