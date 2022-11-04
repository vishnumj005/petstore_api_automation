from behave import step

from features.schema.schema import DELETE_PETS_SCHEMA
from features.service_constants.api_config import ENDPOINTS
from features.services.api_requests import delete_request_service, verify_response_data


@step("DELETE request is sent to delete the existing pets")
def step_impl(context):
    delete_request_service(context,
                           url=f"{ENDPOINTS.DELETE_PETS}{context.pet_id}")


@step("verify delete pets response data")
def step_impl(context):
    verify_response_data(context, DELETE_PETS_SCHEMA)
