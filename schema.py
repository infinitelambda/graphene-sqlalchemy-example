import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType

from database.models import PeopleModel, PlanetModel
from filters import MyFilterableConnectionField


class PeopleAttribute:
    # Generic class for description
    name = graphene.String(description="Name of the person.")
    height = graphene.String(description="Height of the person.")
    mass = graphene.String(description="Mass of the person.")
    hair_color = graphene.String(description="Hair color of the person.")
    skin_color = graphene.String(description="Skin color of the person.")
    eye_color = graphene.String(description="Eye color of the person.")
    birth_year = graphene.String(description="Birth year of the person.")
    gender = graphene.String(description="Gender of the person.")
    planet_id = graphene.ID(description="Global Id of the planet from which the person comes from.")
    url = graphene.String(description="URL of the person in the Star Wars API.")


class PeopleSchema(SQLAlchemyObjectType):
    # People Node
    class Meta:
        model = PeopleModel
        interfaces = (graphene.relay.Node,)
        connection_field_factory = MyFilterableConnectionField.factory


class PeopleConnection(graphene.Connection):
    # People Connection
    class Meta:
        node = PeopleSchema


class PlanetAttribute:
    # Generic class for description
    name = graphene.String(description="Name of the planet.")
    rotation_period = graphene.String(description="Rotation period of the planet.")
    orbital_period = graphene.String(description="Orbital period of the planet.")
    diameter = graphene.String(description="Diameter of the planet.")
    climate = graphene.String(description="Climate period of the planet.")
    gravity = graphene.String(description="Gravity of the planet.")
    terrain = graphene.String(description="Terrain of the planet.")
    surface_water = graphene.String(description="Surface water of the planet.")
    population = graphene.String(description="Population of the planet.")
    url = graphene.String(description="URL of the planet in the Star Wars API.")


class PlanetSchema(SQLAlchemyObjectType):
    # Planet node
    class Meta:
        model = PlanetModel
        interfaces = (graphene.relay.Node,)
        connection_field_factory = MyFilterableConnectionField.factory


class PlanetConnection(graphene.Connection):
    # Planet Connection
    class Meta:
        node = PlanetSchema


class Query(graphene.ObjectType):
    # People queries
    people = graphene.relay.Node.Field(PeopleSchema)
    peopleList = MyFilterableConnectionField(PeopleConnection)

    # Planet queries
    planet = graphene.relay.Node.Field(PlanetSchema)
    planetList = MyFilterableConnectionField(PlanetConnection)


schema = graphene.Schema(query=Query)
