#!/usr/bin/python3
'''use python 3'''

import sys  # the sys module
import hidden_4 as hidden  # import and rename

if __name__ != "__main__":
    exit()

for name in dir(hidden):
    if name[0:2] != "__":
        print(name)
