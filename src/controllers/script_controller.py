import json
from os import environ
from typing import Callable, Dict

from common.exceptions import InvalidPayloadException
from common.validator import validate_schema
from external_services.amqp import AMQPService
from schemas.script import script_post_schema

import flask


def environment(variable, default):
    if value := environ.get(variable, None):
        return value
    return default


class ContextInjector:
    _CONTEXT = {}
    _BROKER_HOST = environment(variable='BROKER_HOST', default='broker')

    def __init__(self, fn: Callable):
        self.fn = fn

    @classmethod
    def get_context(cls):
        if not cls._CONTEXT:
            cls._CONTEXT = {
                'create_amqp_service': AMQPService(
                    exchange='script_topic',
                    host=cls._BROKER_HOST,
                    routing_keys=['script.create.#'],
                ),
            }
        return cls._CONTEXT

    def __call__(self, *args, **kwargs):
        kwargs['context'] = self.get_context()
        return self.fn(*args, **kwargs)


@ContextInjector
def handle_script_create(request: flask.request, context: Dict):
    payload = request.json
    amqp_service = context['create_amqp_service']

    if errors := validate_schema(payload, script_post_schema):
        raise InvalidPayloadException(f'Errors: {errors}')

    amqp_service.publish(topic='script.create', message=payload)
    return amqp_service.wait_consume()


@ContextInjector
def handle_script_retrieve(request: flask.request, context):
    return ''


@ContextInjector
def handle_script_update(request: flask.request, context):
    return ''


@ContextInjector
def handle_script_delete(request: flask.request, context):
    return ''
