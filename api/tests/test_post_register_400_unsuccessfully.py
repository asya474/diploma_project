import jsonschema
import requests
from requests import Response
from api.utils import load_schema

def test_post_register_400_unsuccessfully():
    url = "https://reqres.in/api/register"
    schema = load_schema("json_schemes/post_400.json")

    result: Response = requests.post(url)

    assert result.status_code == 400
    jsonschema.validate(result.json(), schema)