from pprint import pprint


def find_empty_box(board):
    # finds next row,col on the board that's not filled
    # return row,col of empty box

    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col
    return None, None  # if there are no empty fields


def valid_guess(board, guess, row, col):

    # rows check
    if guess in board[row]:
        return False
    # cols check
    col_check = [board[i][col] for i in range(9)]
    if guess in col_check:
        return False
    # 3x3 matrix check

    row_start = (row // 3) * 3
    row_end = row_start + 3

    col_start = (col // 3) * 3
    col_end = col_start + 3

    for row in range(row_start, row_end):
        for col in range(col_start, col_end):
            if board[row][col] == guess:
                return False

    return True


def solve_sudoku(board):
    # if row or col = None then the board is complete
    row, col = find_empty_box(board)
    if row is None:
        return True

    #if not, we try each number from 1-9 and check if the input is valid
    for guess in range(1, 10):
        if valid_guess(board, guess, row, col):
            board[row][
                col] = guess  # if the input is valid we pass it to the board

            if solve_sudoku(board):
                return True

        board[row][
            col] = 0  # board value reset in case the number we passed to the board does not solve the sudooku

    return False


if __name__ == '__main__':
    board = [[7, 0, 0, 0, 0, 9, 0, 0, 0], [0, 0, 0, 6, 0, 0, 0, 4, 0],
             [0, 0, 2, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 4, 0, 0],
             [0, 5, 0, 0, 4, 6, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 6, 0, 0, 0, 0, 0, 5], [2, 0, 0, 5, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 3, 0]]

    print(solve_sudoku(board))
    pprint(board)
