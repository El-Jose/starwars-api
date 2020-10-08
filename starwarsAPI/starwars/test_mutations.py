import pytest

from .data import initializeMovieTests
from starwarsAPI.schema import schema

pytestmark = pytest.mark.django_db


def test_create_movie():
    initializeMovieTests()

    query = """
        mutation {
            createMovie(movieInput: {
                episodeId: 1,
                director: "George Lucas",
                openingText: "La República Galáctica está",
                releaseDate:    "2020-10-06",
                title: "La Amenaza Fantasma",
                planets: [
                  {name: "Tatooine"}
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
