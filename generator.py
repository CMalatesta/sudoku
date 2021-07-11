import numpy as np
from typing import List


def valid_numbers(sudoku:np.ndarray, box_side:int, row: int, column:int) -> List[int]:
    row_start = box_side * (row // box_side)
    row_end = box_side * ((row // box_side) + 1)
    column_start = box_side * (column // box_side)
    column_end = box_side * ((column // box_side) + 1)

    box = sudoku[row_start:row_end, column_start:column_end]

    valid = [
        number
        for number in range(1, sudoku.shape[0]+1)
        if number not in sudoku[row, :]
        if number not in sudoku[:, column]
        if number not in box
    ]

    return valid


if __name__ == "__main__":

    grid_side = 9
    box_side = 3

    rs = np.random.RandomState(seed=11)

    sudoku = np.zeros((grid_side, grid_side), dtype=int)

    fails = -1
    while 0 in sudoku:
        fails += 1
        if fails % 1000 == 0:
            print(f"{fails/1000}k")
        sudoku = np.zeros((grid_side, grid_side), dtype=int)
        location = np.arange(sudoku.size)

        for i in location:
            row = i // sudoku.shape[0]
            column = i % sudoku.shape[0]
            numbers = valid_numbers(sudoku, box_side, row, column)
            if len(numbers) == 0:
                break
            rs.shuffle(numbers)
            sudoku[row, column] = numbers[0]

    # np.save("SudokuPrueba.npy", sudoku)
    print(sudoku)
    print(fails)
