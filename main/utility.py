"""utility function library."""
import os
from pathlib import Path
import json
from .console import console

GET_INT_EXCEPTION = 'An exception occurred while getting the value for an integer parameter'

def get_boolean(param):
    """boolean value from string"""
    ret = param in ('Yes', 'Y', 'True', '1', True, 1)
    return ret

def get_int(param):
    """obtain integer value from string"""
    value = None
    if (not param or param == '0'):
        value = None
    else:
        try:
            value = int(param)
        except Exception as exception:
            console.print(GET_INT_EXCEPTION)
            console.print(exception)
    return value

def get_sequence_file_path(ipath):
    """obtain path for sequence file, helpful for relative file paths"""
    opath = None
    if not os.path.isabs(ipath):
        opath = Path(os.getcwd()) / ipath
    else:
        opath = ipath

    return opath

def write_sequence_file(path):
    """write sequence file"""
    if not os.path.exists(path):
        with open(path, "w", encoding="utf-8") as file:
            empty = {}
            json.dump(empty,file)
