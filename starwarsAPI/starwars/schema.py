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


class CreatePlanet(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()


    class Arguments:
        name = graphene.String()


    def mutate(self, info, name):
        planet = Planet(name=name)
        planet.save()

        return CreatePlanet(
            id=planet.id,
            name=planet.name,
        )


class CreateCharacter(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    height = graphene.String()
    gender = graphene.String()
    homeworld = graphene.String()


    class Arguments:
        name = graphene.String()
        height = graphene.String()
        gender = graphene.String()
        homeworld = graphene.String()


    def mutate(self, info, name, height, gender, homeworld):
        planet_obj = Planet.objects.get(name=homeworld)
        character = Character(name=name, height=height, gender=gender, homeworld=planet_obj)
        character.save()

        return CreateCharacter(
            id=character.id,
            name=character.name,
            height=character.height,
            gender=character.gender,
            homeworld=character.homeworld.name,
        )


class CreateMovie(graphene.Mutation):
    id = graphene.Int()
    episode = graphene.Int()
    director = graphene.String()
    opening_text = graphene.String()
    release_date = graphene.Date()
    title = graphene.String()


    class Arguments:
        pass


    def mutate(self, info, name, height, gender, homeworld):
        pass


class Mutation(graphene.ObjectType):
    create_planet = CreatePlanet.Field()
    create_character = CreateCharacter.Field()
