from behave import step

from features.services.api_commons import build_add_pets_api_payload, create_headers
from features.services.api_requests import post_request_service, verify_response_data
from features.service_constants.api_config import ENDPOINTS
from features.schema.schema import ADD_PETS_SCHEMA


@step("POST request is sent to add new pets with {name}")
def step_impl(context, name):
    header = create_headers()
    api_payload = build_add_pets_api_payload(name)
    post_request_service(context,
                         url=ENDPOINTS.ADD_PETS,
                         payload=api_payload,
                         headers=header)
    context.pet_id = context.res.json()['id']


@step("verify response data")
def step_impl(context):
    verify_response_data(context, ADD_PETS_SCHEMA)
