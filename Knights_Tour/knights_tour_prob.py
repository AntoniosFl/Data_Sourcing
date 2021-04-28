import numpy as np

move_x = [2, 1, -1, -2, -2, -1, 1, 2]
move_y = [1, 2, 2, 1, -1, -2, -2, -1]


def validate_move(board, row, col):
    if row < 8 and row >= 0 and col < 8 and col >= 0 and board[row, col] == 0:
        return True


def solve(board, row, col, n, counter):

    for i in range(n):
        if counter >= (n**2) + 1:
            return True
        new_x = row + move_x[i]
        new_y = col + move_y[i]

        if validate_move(board, new_x, new_y):
            board[new_x, new_y] = counter
            if solve(board, new_x, new_y, n, counter + 1):
                return True
            board[new_x, new_y] = 0

    return False


board = np.zeros((8, 8))

board[3, 2] = 1

solve(board, 3, 2, 8, 2)
print(board.sum())
print(board)
