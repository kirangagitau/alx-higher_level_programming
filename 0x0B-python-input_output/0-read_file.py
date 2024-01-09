#!/usr/bin/python3
"""A funct to read a text file."""


def read_file(filename=""):
    """Print the contents of text file (UTF8) to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
