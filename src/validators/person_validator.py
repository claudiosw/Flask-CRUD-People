from cerberus import Validator

person_validator = Validator({

    "name": {"type": "string", "required": True, "empty": False},
    "age": {"type": "integer", "required": False, "empty": True},
    "neighbourhood": {"type": "string", "required": False, "empty": True},
    "profession": {"type": "string", "required": False, "empty": True}
})
