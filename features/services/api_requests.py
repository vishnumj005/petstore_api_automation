import requests

from features.services import api_commons


def post_request_service(context, url, payload=None, headers=None):
    context.res = requests.post(url=url, data=payload, headers=headers)


def get_request_service(context, url, headers=None, params=None):
    context.res = requests.get(url=url, headers=headers, params=params)


def delete_request_service(context, url, headers=None, params=None):
    context.res = requests.delete(url=url, headers=headers, params=params)


def verify_response_code(context, response_code=None):
    if response_code is not None:
        api_commons.verify_status(context.res, response_code)


def verify_response_data(context, schema):
    api_commons.verify_response(context.res, schema)
