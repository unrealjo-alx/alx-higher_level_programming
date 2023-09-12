#!/usr/bin/python3
"""
12-pascal_triangle: A module providing the pascal_triangle() function.
"""


def pascal_triangle(n):
    """
    Generate and return Pascal's triangle as a list of lists.

    Args:
        n (int): The number of rows in the Pascal's triangle.

    Returns:
        list: List of lists representing Pascal's triangle.
    """
    result = []
    for i in range(0, n):
        row = [1]
        if i == 0:
            result.append(row)
            continue
        if i == 1:
            row.append(1)
        else:
            for current, _next in zip(result[i - 1], result[i - 1][1:]):
                row.append(current + _next)
            row.append(1)
        result.append(row)
    return result
