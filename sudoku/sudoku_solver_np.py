from pprint import pprint


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
    board = [[7, 0, 0, 0, 0, 9, 0, 0, 0], [0, 0, 0, 6, 0, 0, 0, 4, 0],
             [0, 0, 2, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 4, 0, 0],
             [0, 5, 0, 0, 4, 6, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 6, 0, 0, 0, 0, 0, 5], [2, 0, 0, 5, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 3, 0]]
    print(solver(board))
    pprint(board)
