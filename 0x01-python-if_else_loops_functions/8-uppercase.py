#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord(char) > 96 and ord(char) < 223:
            char = chr(ord(char) - 32)
        print(char, end="")
    print("")
