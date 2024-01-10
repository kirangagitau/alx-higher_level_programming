#!/usr/bin/python3
"""JSON file-reading function."""
import json


def load_from_json_file(filename):
    """ loading"""
    with open(filename) as f:
    x = json.load(f)
        return (x)

