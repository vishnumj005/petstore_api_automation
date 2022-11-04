from behave import step
from features.services.api_requests import get_request_service

from features.service_constants.api_config import ENDPOINTS


@step("GET request is sent to find the pets by {status}")
def step_impl(context, status):
    params = {"status": status}
    get_request_service(context,
                        url=ENDPOINTS.FIND_PETS,
                        params=params)
