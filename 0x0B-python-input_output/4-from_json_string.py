#!/usr/bin/python3

import json


def from_json_string(my_str):
    """Return py  obj rep of a JSON string."""
    return json.loads(my_str)
