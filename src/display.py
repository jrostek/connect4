"""
Functions for displaying the game in-console.

display_board - displays the current layout of the board.
"""

import numpy.typing as npt


def print_cell(el: int, col: int, n_cols: int) -> None:
    """Print a specific cell with its contents."""
    el_sign = " "
    if el == 1:
        el_sign = "o"
    elif el == 2:
        el_sign = "x"

    if col < n_cols:
        print("| " + el_sign + " ", end='')
    if col == n_cols - 1:
        print("|", end='')


def display_board(board: npt.NDArray,
                  n_cols: int) -> None:
    """Print out the entire board."""
    row_nums = ["  " + str(x) for x in range(1, n_cols + 1)]
    print("  ", end='')
    print(" ".join(row_nums))

    for i, row in enumerate(board):
        print("  ", end='')
        print("+---" * n_cols + "+")

        print(str(i + 1) + " ", end='')
        for j, elem in enumerate(row):
            print_cell(elem, j, n_cols)
        print("")

    print("  ", end='')
    print("+---" * n_cols + "+")
