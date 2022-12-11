"""
Functions for logic behind gameplay.

play_game - runs the gameplay loop.
"""

import numpy as np
import numpy.typing as npt

from src.display import display_board


def place_piece(board: npt.NDArray,
                row: int,
                col: int,
                player: int,
                n_rows: int,
                n_cols: int) -> bool:
    """Assign a piece its place on the board."""
    try:
        if row < 0 or col < 0:  # negative indices
            raise ValueError("Please choose non-negative indices.")

        if board[row, col] == 0:  # the space is empty
            board[row, col] = player
        else:  # the space is taken
            raise ValueError("There's already a piece in location " +
                  str((row + 1, col + 1)) +
                  ", try again.")
    except IndexError:
        print("Bad placement:", str((row + 1, col + 1)),
              "is outside of board dimensions (" +
              str(n_rows) + " rows and " +
              str(n_cols) + " columns).")
        raise
    except ValueError as error:
        print("Bad placement:", error)
        raise


def four_in_any_row(board: npt.NDArray) -> bool:
    """Return True if there are 4 of the same pieces in one row."""
    ones = "1111"
    twos = "2222"
    for row in board:  # checking rows
        joined_row = "".join(map(str, row))
        if ones in joined_row or twos in joined_row:
            return True
    return False


def switch_player(player_num: int) -> int:
    """Switch current player number."""
    return 2 if player_num == 1 else 1


def game_over(board: npt.NDArray,
              n_cols: int,
              player_num: int) -> bool:
    """Return True if game is finished."""
    player_num = switch_player(player_num)

    # There's no more empty space
    if 0 not in board:
        display_board(board, n_cols)
        print("No space left - nobody won...")
        return True

    # There's a straight line of four pieces of one player
    if four_in_any_row(board):
        display_board(board, n_cols)
        print("Player " + str(player_num) + " won!")
        return True

    board_transposed = board.T  # checking cols
    if four_in_any_row(board_transposed):
        display_board(board, n_cols)
        print("Player " + str(player_num) + " won!")
        return True

    # TODO (additional) Any new piece placement won't result in a win

    # Game not over
    return False


def play_game() -> None:
    """Loop gameplay until a player wins."""
    n_rows = 6
    n_cols = 7
    # 0 - empty cell, 1 - o, 2 - x
    board = np.zeros((n_rows, n_cols), dtype=np.int8)

    print(
        "Welcome to connect four! \n"
        "Place your piece by indicating the location "
        "in the following manner: \n"
        "row,column")
    print("For example, to place a piece in the 3rd row and 2nd column, "
          "enter 3,2 once prompted.")

    player_num = 1
    while not game_over(board, n_cols, player_num):

        display_board(board, n_cols)

        coords = input("Player " +
                       str(player_num) +
                       ": place your piece\n")
        try:
            x, y = map(int, coords.split(","))
        except (TypeError, ValueError) as error:
            print("Incorrectly input placement:", error)
            continue
        try:
            place_piece(board, x - 1, y - 1, player_num, n_rows, n_cols)
        except (IndexError, ValueError):
            continue

        player_num = switch_player(player_num)
