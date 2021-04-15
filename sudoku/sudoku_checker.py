grid = [[7, 8, 4, 1, 5, 9, 3, 2, 6], [5, 3, 9, 6, 7, 2, 8, 4, 1],
        [6, 1, 2, 4, 3, 8, 7, 5, 9], [9, 2, 8, 7, 1, 5, 4, 6, 3],
        [3, 5, 7, 8, 4, 6, 1, 9, 2], [4, 6, 1, 9, 2, 3, 5, 8, 7],
        [8, 7, 6, 3, 9, 4, 2, 1, 5], [2, 4, 3, 5, 6, 1, 9, 7, 8],
        [1, 9, 5, 2, 8, 7, 6, 3, 4]]

comparing_set = set(range(1, 10))


def row_checker():
    for row in range(len(grid)):
        if set(grid[row]) != comparing_set:
            return False
    return True


def col_checker():
    counter = 0
    col_checker = []
    for i in range(len(grid)):
        for j in range(len(grid)):
            col_checker.append(grid[j][counter])
        if set(col_checker) == comparing_set:
            pass
        else:
            print(f'Col No{int(i)+1} is not valid!')
        col_checker = []
        counter += 1
    if counter == 9:
        return True
    else:
        return False


def block_checker_short(start=0):
    if start in [0, 3, 6]:
        block_checker_1 = []
        block_checker_2 = []
        block_checker_3 = []

        counter = start
        end = counter + 3

        while counter < end:
            for i in range(3):
                block_checker_1.append(grid[counter][i])
            for i in range(3, 6):
                block_checker_2.append(grid[counter][i])
            for i in range(6, 9):
                block_checker_3.append(grid[counter][i])
            counter += 1
    else:
        print('Only valid values are 0,3,6')
        return False
    if set(block_checker_1) == comparing_set and set(
            block_checker_2) == comparing_set and set(
                block_checker_3) == comparing_set:
        return True
    else:
        return False


def block_check():
    if block_checker_short(start=0) and block_checker_short(
            start=3) and block_checker_short(start=6):
        return True


def main(grid):
    if block_check() and row_checker() and col_checker():
        print('This Sudoku is valid')
    else:
        print('This Sudoklu is not valid')


if __name__ == '__main__':
    main(grid)
