#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    secret = dir(hidden_4)
    for item in secret:
        if not item.startswith("__"):
            print(item)
