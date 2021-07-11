import numpy as np
from typing import List, Tuple
from generator import valid_numbers


def get_candidates(sudoku: np.ndarray, box_side: int) -> np.ndarray:
    candidate = np.zeros([sudoku.shape[0]] * 3, dtype=bool)

    for i in range(sudoku.size):
        row, column = np.unravel_index(i, sudoku.shape)
        if sudoku[row, column] == 0:
            for j in valid_numbers(sudoku, box_side, row, column):
                candidate[row, column, j - 1] = True
    return candidate


def filter_uniques(candidates: np.ndarray) -> List[Tuple[int, int, int]]:
    filter = [
        (row, column, np.argmax(candidates[row, column, :]) + 1)
        for row, column in [
            (i // candidates.shape[0], i % candidates.shape[0])
            for i in range(candidates.shape[0]**2)
        ]
        if np.sum(candidates[row, column, :]) == 1
    ]
    return filter


def solve(input_sudoku: np.ndarray, box_side: int) -> np.ndarray:
    sudoku = np.copy(input_sudoku)
    while 0 in sudoku:
        candidates = get_candidates(sudoku, box_side)
        filtered = filter_uniques(candidates)
        if not filtered:
            print("There aren't uniques values")
            break
        for row, column, value in filtered:
            sudoku[row, column] = value
    return sudoku


if __name__ == "__main__":
    box_side = 3

    original_sudoku = np.array([
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ])

    sudoku = np.copy(original_sudoku)

    solve_sudoku = solve(sudoku, box_side)
    print(sudoku)
    print(original_sudoku[original_sudoku > 0].size)