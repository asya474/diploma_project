import requests
from requests import Response


def test_delete_204_succesfully(browser_setup):
    url = "https://reqres.in/api/users/2"

    result: Response = requests.delete(url)

    assert result.status_code == 204
