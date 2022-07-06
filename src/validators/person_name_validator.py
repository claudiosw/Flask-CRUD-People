from cerberus import Validator

person_name_validator = Validator({
    "name": {"type": "string", "required": True, "empty": False}
})
