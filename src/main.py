from flask import Flask, abort

app = Flask(__name__)


SCRIPT_CONTROLLER_MAPPING = {
    'GET': None,
    'POST': None,
    'PUT': None,
    'DELETE': None,
}


@app.route('/api/v1/scripts', method=['GET', 'POST', 'PUT', 'DELETE'])
def scripts_endpoint():
    try:
        return SCRIPT_CONTROLLER_MAPPING[request.method](request)
    except KeyError:
        abort(405)
