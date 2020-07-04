from datetime import datetime, timedelta
from flask import request, abort
import random
import string
import re
from random import randint
from cerberus import Validator


def generate_timestamp():
    return datetime.utcnow().isoformat()


def generate_expiry_date(year: int):
    return datetime.now() + timedelta(days=year * 365)


def generate_key(length):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))


def generate_unique_key(key: str):
    t = str(datetime.now().timestamp()).split(".")
    ts = t[0] + t[1]
    return key[:24] + ts


def generate_16_digit(prefix: str):
    for i in range(12):
        prefix = prefix + str(randint(0, 9))
    return prefix


def generate_4_digit():
    num = ""
    for i in range(4):
        num = num + str(randint(0, 9))
    return num


def validate_request(required_params, expected_params, to_be_checked):
    if not request.json:
        abort(400, "Request should be in JSON format")
    # Check if not all required parameter exist in the request JSON body
    if not all(expected_param in to_be_checked for expected_param in expected_params):
        abort(400, "One or more expected param is missing")
    # Check if any of the required params value is empty
    for key in required_params:
        if to_be_checked[key] is None or to_be_checked[key] == "":
            abort(400, "One or more required param is empty")
    return None


def validate_request_schema(schema, json_object):
    validator = Validator(schema)
    if not request.json:
        abort(400, "Request should be in JSON format")
    if not validator.validate(json_object):
        abort(400, str(validator.errors))
    return True


def lower_object(obj, keys: list):
    for k in keys:
        obj[k] = obj[k].lower()
    return obj


def is_base64_encoded(s):
    return re.search("^([A-Za-z0-9+/]{4})*([A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{2}==)?$", s)


