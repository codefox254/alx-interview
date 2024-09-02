#!/usr/bin/python3
import sys


def print_solution(queens):
    """Prints the solution in the required format."""
    print([[i, queens[i]] for i in range(len(queens))])


def is_safe(queens, row, col):
    """Checks if a queen can be placed at (row, col)."""
    for r in range(row):
        c = queens[r]
        # Check if queens are in the same column or diagonal
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True


def solve_nqueens(N):
    """Solves the N queens problem using backtracking."""
    def backtrack(row):
        if row == N:
            print_solution(queens)
            return
        for col in range(N):
            if is_safe(queens, row, col):
                queens[row] = col
                backtrack(row + 1)

    queens = [-1] * N
    backtrack(0)


def main():
    # Check the number of command line arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Validate N
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Ensure N is at least 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Solve the N queens problem
    solve_nqueens(N)


if __name__ == "__main__":
    main()
