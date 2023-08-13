#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return

    x_len = len(matrix)
    y_len = 0
    if x_len > 0:
        y_len = len(matrix[0])

    for i in range(x_len):
        for j in range(y_len):
            print("{:d}".format(matrix[i][j]), end="")
            if j != y_len - 1:
                print(" ", end="")
        print("")
