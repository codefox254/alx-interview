#!/usr/bin/python3
"""
The pascal_triangle
"""

def pascal_triangle(n):
    if n <= 0:
        return []
    
    triangle = [[1]]  # Start with the first row of the triangle
    
    for i in range(1, n):
        row = [1]  # Start the row with a 1
        # Compute the intermediate values
        prev_row = triangle[-1]
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)  # End the row with a 1
        triangle.append(row)
    
    return triangle
