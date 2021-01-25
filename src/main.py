from flask import Flask, abort, request

from controllers import script_controller
from common.exceptions import InvalidPayloadException


SCRIPT_CONTROLLER_MAPPING = {
    'GET': script_controller.handle_script_retrieve,
    'POST': script_controller.handle_script_create,
    'PUT': script_controller.handle_script_update,
    'DELETE': script_controller.handle_script_delete,
}


def create_app():
    app = Flask(__name__)

    @app.route('/api/v1/script', methods=['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS', 'HEAD'])
    def scripts_endpoint():
        try:
            return SCRIPT_CONTROLLER_MAPPING[request.method](request)
        except InvalidPayloadException:
            abort(400)
        except KeyError:
            abort(405)

    return app


app = create_app()
