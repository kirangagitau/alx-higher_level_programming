#!/usr/bin/python3

import json


def from_json_string(my_str):
    """Return py  obj rep of a JSON string."""
    str = json.loads(my_str)
    return (str)
