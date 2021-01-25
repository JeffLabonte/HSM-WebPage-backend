from common.validator import validate_schema
from schemas.script import script_post_schema

import pytest


@pytest.mark.parametrize('payload, has_error', [
    (
        {
            'name': 'Test',
            'repository': 'git@github.com:JeffLabonte/Test.git',
            'exec': './src/exec.sh',
        },
        False,
    ),
    (
        {
            'repository': 'git@github.com:JeffLabonte/Test.git',
            'exec': './src/exec.sh',
        },
        True,
    ),
    (
        {
            'name': 'Test',
            'repository': 'git@github.com:Jeff_Labont.2/tEs32.git',
            'exec': './src/exec.sh',
        },
        False,
    ),
    (
        {
            'name': 'Test',
            'repository': 'git@github.com:Jeff_Labont.2/tEs32.git',
        },
        True,
    ),
    (
        {
            'name': 'Test',
            'repository': 'not a git repo',
            'exec': 'python src/script.py',
        },
        True,
    ),
])
def test_script_post_schema__validate_payload__should_match_expected(payload, has_error):
    result = validate_schema(payload, script_post_schema)
    assert bool(result) == has_error
