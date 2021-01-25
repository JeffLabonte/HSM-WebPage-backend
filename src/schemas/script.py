script_post_schema = {
    "name": {
        "type": "string",
        "min": 1,
        "max": 40,
        "required": True,
    },
    "repository": {
        "type": "string",
        "regex": "^(git@github.com:)[A-Za-z0-9-_.]+/[A-Za-z0-9-_.]+.git$",
        "required": True,
    },
    "exec": {
        "type": "string",
        "required": True,
    }
}
