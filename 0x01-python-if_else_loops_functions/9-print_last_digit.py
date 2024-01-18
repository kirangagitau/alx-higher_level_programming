#!/usr/bin/python3
'''use python3'''


def print_last_digit(number):
    no = number
    if no < 0:
        ld = no % -(10)
        print(-(ld), end="")
    else:
        ld = no % 10
        print(ld, end="")
    return abs(ld)
