def find_empty_box(board):
  # finds next row,col on the board that's not filled
  # return row,col of empty box

  for row in range(9):
    for col in range(9):
      if board[row][col] != 0:
        return row,col
  return None, None # if there are no empty fields

def valid_guess(board, guess, row,col):

  # rows check
  if guess in board[row]:
    return False
  # cols check
  col_check = [board[i][col] for i in range(9)]
  if guess in col_check:
    return False
  # 3x3 matrix check

def solve_sudoku(board):
  # if row or col = None then the board is complete
  row,col = find_empty_box(board)
  if row is None:
    return True

  #if not we won't to try each number from 1-9 and check if the input is valid
  for guess in range(1,10):
    if valid_guess(board, guess, row,col)



