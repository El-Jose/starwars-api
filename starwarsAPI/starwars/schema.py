import graphene
from django.db.models import Q
from graphene_django import DjangoObjectType, DjangoListField
from .models import Character, Planet, Producer, Movie


class CharacterType(DjangoObjectType):
    class Meta:
        model = Character
        fields = "__all__"


class PlanetType(DjangoObjectType):
    class Meta:
        model = Planet
        fields = "__all__"


class ProducerType(DjangoObjectType):
    class Meta:
        model = Producer
        fields = "__all__"


class MovieType(DjangoObjectType):
    class Meta:
        model = Movie
        fields = "__all__"


class Query(graphene.ObjectType):
    characters = DjangoListField(CharacterType, search=graphene.String())
    planets = graphene.List(PlanetType)

    def resolve_characters(self, info, search=None, **kwargs):
        if search:
            f = (Q(name__contains=search))
            return Character.objects.filter(f)

        return Character.objects.all()

    def resolve_planets(self, info, **kwargs):
        return Planet.objects.all()
