#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if i != j and i < j and i * 10 + 9 != 89:
            print("{}{}, ".format(i, j), end="")
print("89")
