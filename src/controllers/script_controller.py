import flask

from common.exceptions import InvalidPayloadException
from common.validator import validate_schema
from schemas.script import script_post_schema


def handle_script_create(request: flask.request):
    payload = request.json
    if errors := validate_schema(payload, script_post_schema):
        raise InvalidPayloadException(f'Errors: {errors}')

    return ''


def handle_script_retrieve(request: flask.request):
    return ''


def handle_script_update(request: flask.request):
    return ''


def handle_script_delete(request: flask.request):
    return ''
