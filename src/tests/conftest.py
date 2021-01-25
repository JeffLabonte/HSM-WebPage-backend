from main import create_app

import pytest


@pytest.fixture(scope='session')
def app():
    return create_app()
