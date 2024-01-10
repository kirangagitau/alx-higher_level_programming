#!/usr/bin/python3

import json

def save_to_json_file(my_obj, filename):
    ''' first convert object to JSON file'''
    jstr = json.dumps(my_obj)

    '''open the file to which to write'''
    with open("filename", "w") as file
    file.write(jstr)
    return
