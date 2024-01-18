def test_put_update_200_succesfully():
    url = "https://reqres.in/api/users/2"
    schema = load_schema("json_schemes/put_update.json")

    result: Response = requests.put(url)

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)