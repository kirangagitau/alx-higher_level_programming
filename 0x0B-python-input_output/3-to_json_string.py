#!/usr/bin/python3

import json


def to_json_string(my_obj):
    '''encoding into a JavaScript Objects Notation'''
    j_str = json.dumps(my_obj)
    return (j_str)
