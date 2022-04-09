import os
from pathlib import Path
import json

def get_boolean(param):
	return True if param == 'Yes' or param == 'Y' or param == 'True' or param == '1' or param == True else False

def get_int(param):
	value = None
	if (not param or param == '0'):
		value = None
	else:
		try:
			value = int(param)
		except Exception as e:
			console.print("An exception occurred while getting the value for an integer parameter")
			console.print(e)
	return value

def get_sequence_file_path(ipath):
	opath = None
	if not os.path.isabs(ipath):
		opath = Path(os.getcwd()) / ipath
	else:
		opath = ipath

	return opath

def write_sequence_file(path):
	if not os.path.exists(path):
		with open(path, "w") as f:
			empty = {}
			json.dump(empty,f)


