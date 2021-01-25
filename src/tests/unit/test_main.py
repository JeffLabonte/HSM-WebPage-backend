from unittest.mock import MagicMock, patch

import pytest
import requests
from flask import url_for


MOCKED_CONTROLLER_MAPPING = {
    'GET': MagicMock,
    'PUT': MagicMock,
    'POST': MagicMock,
    'DELETE': MagicMock,
}


@pytest.mark.usefixtures('live_server')
class TestLiveTest():

    @patch.dict('main.SCRIPT_CONTROLLER_MAPPING', MOCKED_CONTROLLER_MAPPING, clear=True)
    @pytest.mark.parametrize('method, request_method', [
        ('GET', requests.get,),
        ('PUT', requests.put,),
        ('POST', requests.post,),
        ('DELETE', requests.delete,),
    ])
    def test_scripts_endpoint__should_calls_mock_function(self, method, request_method):
        dict_key = method.upper()
        res = request_method(url_for('scripts_endpoint', _external=True))
        assert MOCKED_CONTROLLER_MAPPING[dict_key].called


@pytest.mark.parametrize('method', [
    'head',
    'options'
])
def test_scripts_endpoint__should_return_405_code(method, client):
    res = getattr(client, method)('/api/v1/script')
    assert res.status_code == 405
