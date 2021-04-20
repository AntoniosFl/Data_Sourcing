from pprint import pprint
import numpy as np


def valid_inp(grid, row, col, num):
    for i in range(0, 9):
        if grid[row][i] == num:
            return False
    for i in range(0, 9):
        if grid[i][col] == num:
            return False
    row_new = (row // 3) * 3
    col_new = (col // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[row_new + i][col_new + j] == num:
                return False
    return True


def solver(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for num in range(1, 10):
                    if valid_inp(grid, row, col, num):
                        grid[row][col] = num
                        solver(grid)
                        grid[row][col] = 0
                return
    print(np.matrix(grid))
    input("Want more solutions?")


if __name__ == "__main__":
    board = grid = [[5, 3, 0, 0, 7, 0, 0, 0, 0], [6, 0, 0, 1, 9, 5, 0, 0, 0],
                    [0, 9, 8, 0, 0, 0, 0, 6, 0], [8, 0, 0, 0, 6, 0, 0, 0, 3],
                    [4, 0, 0, 8, 0, 3, 0, 0, 1], [7, 0, 0, 0, 2, 0, 0, 0, 6],
                    [0, 6, 0, 0, 0, 0, 2, 8, 0], [0, 0, 0, 4, 1, 9, 0, 0, 5],
                    [0, 0, 0, 0, 8, 0, 0, 7, 9]]
    print(solver(board))
