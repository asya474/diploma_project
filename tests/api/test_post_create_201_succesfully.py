import jsonschema
import requests
from requests import Response
from helper.api_helpers.utils import load_schema

def test_post_create_201_succesfully():
    url = "https://reqres.in/api/users"
    schema = load_schema("json_schemes/post_create.json")

    result: Response = requests.post(url)

    assert result.status_code == 201
    jsonschema.validate(result.json(), schema)







