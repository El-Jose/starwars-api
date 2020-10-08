from .models import Character, Planet, Producer, Movie


def initializeMovieTests():
    planet = Planet.objects.get_or_create(name="Tatooine")

def initializePlanetTest():
    planet = Planet.objects.get_or_create(name="Andromeda")