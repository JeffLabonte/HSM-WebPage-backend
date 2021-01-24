from flask import Flask, abort, request

import controllers

app = Flask(__name__)


SCRIPT_CONTROLLER_MAPPING = {
    'GET': None,
    'POST': controllers.handle_script_create,
    'PUT': None,
    'DELETE': None,
}


@app.route('/api/v1/scripts', methods=['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'])
def scripts_endpoint():
    try:
        return SCRIPT_CONTROLLER_MAPPING[request.method](request)
    except KeyError:
        abort(405)
