Task: Solving the N Queens Problem
The N Queens problem involves placing N queens on an N×N chessboard such that no two queens threaten each other. This means no two queens share the same row, column, or diagonal.

Requirements
Usage: The program is run with nqueens N, where N is the size of the board (NxN) and the number of queens.
Input Validation:
If the wrong number of arguments is provided, print Usage: nqueens N and exit with status 1.
If N is not an integer, print N must be a number and exit with status 1.
If N is less than 4, print N must be at least 4 and exit with status 1.
Output:
Print every possible solution on a new line.
Each solution should be formatted as a list of positions [row, col] for each queen.
