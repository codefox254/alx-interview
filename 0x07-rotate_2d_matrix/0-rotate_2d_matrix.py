#!/usr/bin/python3
"""
This module contains a function to rotate a 2D matrix 90 degrees clockwise.
"""

def rotate_2d_matrix(matrix):
    """
    Rotates a given n x n 2D matrix 90 degrees clockwise in place.
    
    Args:
        matrix (list of list of int): The 2D matrix to rotate.
        
    Returns:
        None: The matrix is rotated in place.
    """
    n = len(matrix)
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            # Store the top element
            top = matrix[i][j]

            # Move left element to top
            matrix[i][j] = matrix[n - 1 - j][i]

            # Move bottom element to left
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]

            # Move right element to bottom
            matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]

            # Assign top element to right
            matrix[j][n - 1 - i] = top

# Example usage
if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    rotate_2d_matrix(matrix)
    print(matrix)
