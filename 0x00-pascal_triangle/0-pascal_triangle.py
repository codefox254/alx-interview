#!/usr/bin/python3
# 0-pascal_triangle

def pascal_triangle(n):
    """
    Returns a list of lists of integers
    representing the Pascal's triangle of n.
    Returns an empty list if n <= 0.
    """
    triangle = []
    if n <= 0:
        return triangle
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(len(triangle[i - 1]) - 1):
            row.append(triangle[i - 1][j] + triangle[i - 1][j + 1])
        row.append(1)
        triangle.append(row)
    return triangle
