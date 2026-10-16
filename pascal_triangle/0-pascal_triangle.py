#!/usr/bin/python3
"""Pascal's triangle: build the first n rows as a list of lists."""


def pascal_triangle(n):
    """Return a list of lists of integers representing Pascal's triangle.

    Each row starts and ends with 1, and every other value is the sum
    of the two values above it in the previous row. Returns an empty
    list if n is less than or equal to 0.
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for _ in range(1, n):
        previous = triangle[-1]
        row = [1]
        for i in range(1, len(previous)):
            row.append(previous[i - 1] + previous[i])
        row.append(1)
        triangle.append(row)
    return triangle
