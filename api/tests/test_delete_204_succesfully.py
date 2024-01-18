def test_delete_204_succesfully():
    url = "https://reqres.in/api/users/2"

    result: Response = requests.delete(url)

    assert result.status_code == 204