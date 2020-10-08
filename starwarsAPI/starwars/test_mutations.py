import json
import pytest

from .data import initializeDummyPlanet
from starwarsAPI.schema import schema

pytestmark = pytest.mark.django_db


def test_create_movie():
    initializeDummyPlanet()

    query = """
        mutation {
            createMovie(movieInput: {
                episodeId: 1,
                director: "George Lucas",
                openingText: "La República Galáctica está",
                releaseDate:    "2020-10-06",
                title: "La Amenaza Fantasma",
                planets: [
                  {name: "Dummy planet"}
                ]
              }) {
                movie{
                  id
                  episodeId
                  title
                  planets {
                    id
                    name
                  }
                }
            } 
        }
    """

    result = schema.execute(query)
    assert not result.errors

def test_create_movie_unexisting_planet():

    query = """
        mutation {
            createMovie(movieInput: {
                episodeId: 1,
                director: "George Lucas",
                openingText: "La República Galáctica está",
                releaseDate:    "2020-10-06",
                title: "La Amenaza Fantasma",
                planets: [
                  {name: "Planet express"}
                ]
              }) {
                movie{
                  id
                  episodeId
                  title
                  planets {
                    id
                    name
                  }
                }
            } 
        }
    """

    result = schema.execute(query)
    assert result.errors

def test_create_movie_validate_fields_types():

    query = """
        mutation {
            createMovie(movieInput: {
                episodeId: "fsadfadf",
                director: 1,
                openingText: 1,
                releaseDate: "dsfsdf",
                title: 1,
                planets: [
                  {name: 1}
                ]
              }) {
                movie{
                  id
                  episodeId
                  title
                  planets {
                    id
                    name
                  }
                }
            } 
        }
    """

    result = schema.execute(query)
    assert result.errors
    assert "invalid value" in result.errors[0].message
    assert "Expected type \"String\"" in result.errors[0].message
    assert "Expected type \"Int\"" in result.errors[0].message

def test_create_planet():

    query = """
        mutation {
          createPlanet(name: "Andromeda") {
            name
          }
        }
    """

    response = {
        "createPlanet": {
            "name": "Andromeda"
        }
    }

    result = schema.execute(query)
    output_dict = json.loads(json.dumps(result.data))
    assert output_dict == response
    assert not result.errors

def test_create_existing_planet():
    initializeDummyPlanet()

    query = """
        mutation {
          createPlanet(name: "Dummy planet") {
            name
          }
        }
    """

    response = {
        "createPlanet": {
            "name": "Dummy planet"
        }
    }

    result = schema.execute(query)
    output_dict = json.loads(json.dumps(result.data))
    assert output_dict == response
    assert not result.errors

def test_create_planet_validate_field_type():

    query = """
        mutation {
          createPlanet(name: 4534534534534) {
            name
          }
        }
    """

    result = schema.execute(query)
    assert result.errors
    assert "Expected type \"String\"" in result.errors[0].message

def test_create_character():

    query = """
        mutation {
            createCharacter(
              gender: "Male",
              height: "1.34 m",
              homeworld: "New planet",
              name: "Juanito"
            ) {
              name
              homeworld
            }
        }
    """

    response = {
        "createCharacter": {
            "name": None,
            "homeworld": None
        }
    }

    result = schema.execute(query)
    output_dict = json.loads(json.dumps(result.data))
    assert output_dict == response
    assert not result.errors


def test_create_character_validate_fields_type():

    query = """
        mutation {
            createCharacter(
              gender: 345345,
              height: 34343,
              homeworld: 45345,
              name: 76867
            ) {
              name
              homeworld
            }
        }
    """

    result = schema.execute(query)
    assert result.errors
    assert "Expected type \"String\"" in result.errors[0].message