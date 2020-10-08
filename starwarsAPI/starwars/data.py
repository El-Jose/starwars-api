from .models import Character, Planet, Producer, Movie


def initializeDummyPlanet():
    planet = Planet.objects.get_or_create(name="Dummy planet")
