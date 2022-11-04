import json
from jsonschema import validate


def verify_status(response, expected_code):
    assert response.status_code == int(expected_code), \
        f'Expected status code:{expected_code},' \
        f' but was: {response.status_code} with body: {response.text} for {response.request.method} {response.url}'
    if response.status_code != int(expected_code):
        print(response)


def verify_response(response, schema):
    try:
        validate(instance=response.json(), schema=schema)
    except Exception as e:
        assert False, "Invalid Response"


def create_headers():
    return {
        'Content-Type': "application/json"
    }


def build_add_pets_api_payload(name, status="available"):
    return json.dumps({
        "name": name,
        "photoUrls": [
            "string"
        ],
        "status": status
    })

