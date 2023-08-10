#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    num_args = len(argv) - 1
    if num_args == 0:
        print("0 arguments.")
    else:
        print("{} arguments:".format(num_args))
        # Skip the first arg (name of the file)
    for index, arg in enumerate(argv[1:], 1):
        print("{:d}: {}".format(index, arg))
