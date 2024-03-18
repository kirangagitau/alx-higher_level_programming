#!/usr/bin/python3
"""Defining Python class-to-JSON function."""


def class_to_json(obj):
    """Returning the dict rep of a simple data structure."""
    return obj.__dict__
