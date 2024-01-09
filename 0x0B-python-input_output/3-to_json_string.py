#!/usr/bin/python3
import json
"""use python3 interpreter for thi code"""
"""Defining string-to-JSON function."""


def to_json_string(my_obj):
    """Return the JSON rep of a string object."""
    return json.dumps(my_obj)
