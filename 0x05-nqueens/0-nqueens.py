#!/usr/bin/env python3

import sys


def is_safe(board, row, col, N):
    # Check the column
    for i in range(row):
        if board[i][1] == col:
            return False
        # Check diagonals
        if abs(board[i][1] - col) == abs(i - row):
            return False
    return True


def solve_nqueens(board, row, N):
    if row == N:
        print(board)
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            board.append([row, col])
            solve_nqueens(board, row + 1, N)
            board.pop()


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens([], 0, N)


if __name__ == "__main__":
    main()
