import json
import pytest
from graphene_django.utils.testing import graphql_query

@pytest.fixture
def client_query(client):
    def func(*args, **kwargs):
        return graphql_query(*args, **kwargs, client=client)

    return func

def test_insert_movie(client_query):
    response = client_query(
        '''
		mutation {
		    createMovie(movieInput: {
		        episodeId: 1,
		        director: "George Lucas",
		        openingText: "La República Galáctica está",
		        releaseDate: 	"2020-10-06",
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
        ''',
        op_name='myModel'
    )

    content = json.loads(response.content)
    assert 'errors' not in content