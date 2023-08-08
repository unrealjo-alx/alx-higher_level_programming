#!/usr/bin/python3
for i in range(97, 123):
    # 101 is for e, and 113 for q
    if i != 101 and i != 113:
        print("{:c}".format(i), end="")
