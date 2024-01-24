import jsonschema
import requests
from requests import Response

from helper.api_helpers.utils import load_schema


def test_get_single_user_successfully():
    url = "https://reqres.in/api/users/2"
    schema = load_schema("json_schemes/get_single_user.json")

    result: Response = requests.get(url)

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
