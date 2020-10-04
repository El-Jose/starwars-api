import graphene
from graphene_django import DjangoObjectType

from .models import Link


class LinkType(DjangoObjectType):
    pass


class Query(graphene.ObjectType):
    pass