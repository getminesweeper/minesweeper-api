import pytest
from minesweeper_api.domain.entities.minesweeper_game_board import (
    MinesweeperGameBoard,
)
from minesweeper_api.domain.entities.minesweeper_board_box import (
    MinesweeperBoardBox,
)
from minesweeper_api.domain.value_objects.game_difficulty import (
    GameDifficulty,
)


def test_should_create_minesweeper_game_board_when_correct_values_are_given():
    minesweeper_game_board = MinesweeperGameBoard(5, 7, GameDifficulty.EASY)

    assert minesweeper_game_board.board_boxes
    assert minesweeper_game_board.rows == 5
    assert minesweeper_game_board.cols == 7


def test_board_boxes_should_be_instance_of_board_box():
    minesweeper_game_board = MinesweeperGameBoard(5, 7, GameDifficulty.EASY)
    board_boxes = minesweeper_game_board.board_boxes

    for row in range(minesweeper_game_board.rows):
        for col in range(minesweeper_game_board.cols):
            assert isinstance(board_boxes[row][col], MinesweeperBoardBox)


def test_should_calculete_right_amount_of_mines_when_game_difficulty_is_easy():
    minesweeper_game_board = MinesweeperGameBoard(6, 8, GameDifficulty.EASY)
    assert minesweeper_game_board.amount_of_mines == 5


def test_should_calculete_right_amount_of_mines_when_game_difficulty_is_med():
    minesweeper_game_board = MinesweeperGameBoard(6, 8, GameDifficulty.MEDIUM)
    assert minesweeper_game_board.amount_of_mines == 24


def test_should_calculete_right_amount_of_mines_when_game_difficulty_is_hard():
    minesweeper_game_board = MinesweeperGameBoard(6, 8, GameDifficulty.HARD)
    assert minesweeper_game_board.amount_of_mines == 36


def test_should_not_create_minesweeper_game_board_when_min_rows_is_invalid():
    with pytest.raises(
        ValueError,
        match="The minimum amount of rows and cols to be configured is 3",
    ):
        MinesweeperGameBoard(2, 10, GameDifficulty.EASY)


def test_should_not_create_minesweeper_game_board_when_min_cols_is_invalid():
    with pytest.raises(
        ValueError,
        match="The minimum amount of rows and cols to be configured is 3",
    ):
        MinesweeperGameBoard(10, 2, GameDifficulty.EASY)


def test_should_not_create_minesweeper_game_board_when_max_rows_is_invalid():
    with pytest.raises(
        ValueError,
        match="The maximum amount of rows and cols to be configured is 17",
    ):
        MinesweeperGameBoard(20, 10, GameDifficulty.EASY)


def test_should_not_create_minesweeper_game_board_when_max_cols_is_invalid():
    with pytest.raises(
        ValueError,
        match="The maximum amount of rows and cols to be configured is 17",
    ):
        MinesweeperGameBoard(10, 20, GameDifficulty.EASY)
