import jsonschema
import requests
from requests import Response

from helper_for_test.api_helpers.utils import load_schema


def test_post_create_201_succesfully(browser_setup):
    url = "https://reqres.in/api/users"
    schema = load_schema("post_create.json")

    result: Response = requests.post(url)

    assert result.status_code == 201
    jsonschema.validate(result.json(), schema)
