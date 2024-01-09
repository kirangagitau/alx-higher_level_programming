#!/usr/bin/python3
"""interpret using the python 3"""
"""Defines a file-appending function."""


def append_write(filename="", text=""):
    """Appends a string to the end of text file(UTF) .
    Args:
        filename (str):name of file to append to.
        text (str): The string to append
    Returns:
        no of chars appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
