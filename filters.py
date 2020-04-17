from graphene_sqlalchemy_filter import FilterableConnectionField, FilterSet
from database.models import PeopleModel, PlanetModel


class PeopleFilter(FilterSet):
    class Meta:
        model = PeopleModel
        fields = {'name': ['eq', 'ne', 'in', 'ilike'],
                  'planet_id': ['eq', 'ne', 'in', 'gt', 'lt', 'gte', 'lte']}


class PlanetsFilter(FilterSet):
    class Meta:
        model = PlanetModel
        fields = {'id': [...],  # shortcut!
                  'name': ['eq', 'ne', 'in', 'ilike']}


class MyFilterableConnectionField(FilterableConnectionField):
    filters = {PeopleModel: PeopleFilter(), PlanetModel: PlanetsFilter()}
