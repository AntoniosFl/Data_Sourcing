import numpy as np


def validate(board, n):

    for row in range(0, n):
        if sum(board[row, ]) > 1:
            return False

    for col in range(0, n):
        if sum(board[:, col]) > 1:
            return False

    diags = [board[::-1, :].diagonal(i) for i in range(-n + 2, n - 1)]
    diags.extend(board.diagonal(i) for i in range(n - 2, -n + 1, -1))

    for x in diags:
        if sum(x) > 1:
            return False
    return True


def solve(board, col, n):

    if validate(board, n):
        if board.sum() == n:
            return True

    for row in range(0, n):
        board[row, col] = 1
        if validate(board, n):
            if solve(board, col + 1, n):
                return True
            board[row, col] = 0
        else:
            board[row, col] = 0
    return False


board = np.zeros((8, 8))
if solve(board, 0, 8):
    print(board)
