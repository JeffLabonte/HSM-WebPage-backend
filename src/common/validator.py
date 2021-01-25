from cerberus import Validator

from typing import Dict


def validate_schema(dirty_input: Dict, schema: Dict) -> Dict:
    """
    Empty dict means that there no errors.
    """
    v = Validator()
    v.validate(dirty_input, schema)
    return v.errors
