import numpy as np
from typing import List

grid_side = 9
box_side = 3

sudoku = np.zeros((grid_side, grid_side), dtype=int)

def valid_numbers(row: int, column:int) -> List[int]:
    row_start = box_side * (row // box_side)
    row_end = box_side * ((row // box_side) + 1)
    column_start = box_side * (column // box_side)
    column_end = box_side * ((column // box_side) + 1)

    box = sudoku[row_start:row_end, column_start:column_end]

    valid = [
        number
        for number in range(1, grid_side+1)
        if number not in sudoku[row, :]
        if number not in sudoku[:, column]
        if number not in box
    ]

    return valid






fails = -1
while 0 in sudoku:
    fails += 1
    if fails % 1000 == 0:
        print(f"{fails/1000}k")
    sudoku = np.zeros((grid_side, grid_side), dtype=int)
    location = np.arange(sudoku.size)
    np.random.shuffle(location)

    for i in location:
        row = i // grid_side
        column = i % grid_side
        numbers = valid_numbers(row, column)
        if len(numbers) == 0:
            break
        np.random.shuffle(numbers)
        sudoku[row, column] = numbers[0]

print(sudoku)
print(fails)
