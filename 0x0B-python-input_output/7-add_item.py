#!/usr/bin/python3

"""A script that adds all arguments to a Python list,
and then save them to a file:

"""
import sys
import os

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

if __name__ == "__main__":
    FILE_NAME = "add_item.json"
    args_list = []

    if not os.access(FILE_NAME, os.R_OK):
        save_to_json_file(args_list, FILE_NAME)

    if len(sys.argv) > 1:
        args_list = load_from_json_file(FILE_NAME)
        args_list.extend(sys.argv[1:])
        save_to_json_file(args_list, FILE_NAME)
