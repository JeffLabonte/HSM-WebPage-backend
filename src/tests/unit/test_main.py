from unittest.mock import MagicMock, patch

import pytest
from flask import url_for


@pytest.mark.parametrize('method', [
    'get',
    'put',
    'post',
    'delete',
])
def test_scripts_endpoint__should_return_200_and_call_function(method, client):
    dict_key = method.upper
    with patch.dict('main.SCRIPT_CONTROLLER_MAPPING', {dict_key: MagicMock}) as mocked_function:
        res = getattr(client, method)('/api/v1/script')
        assert mocked_function[dict_key].called
        assert res.status_code == 200


@pytest.mark.parametrize('method', [
    'head',
    'options'
])
def test_scripts_endpoint__should_return_405_code(method, client):
    res = getattr(client, method)('/api/v1/script')
    assert res.status_code == 405
