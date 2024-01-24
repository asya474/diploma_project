import jsonschema
import requests
from requests import Response

from helper.api_helpers.utils import load_schema


def test_put_update_200_succesfully(browser_setup):
    url = "https://reqres.in/api/users/2"
    schema = load_schema("put_update.json")

    result: Response = requests.put(url)

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)