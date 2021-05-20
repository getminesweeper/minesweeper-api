import pytest
from minesweeper_api.domain.entities.minesweeper_game_board import (
    MinesweeperGameBoard,
)
from minesweeper_api.domain.entities.minesweeper_board_box import (
    MinesweeperBoardBox,
)


def test_should_create_minesweeper_game_board_when_correct_values_are_given():
    minesweeper_game_board = MinesweeperGameBoard(5, 7)

    assert minesweeper_game_board.board_boxes
    assert minesweeper_game_board.rows == 5
    assert minesweeper_game_board.cols == 7


def test_board_boxes_should_be_instance_of_board_box():
    minesweeper_game_board = MinesweeperGameBoard(5, 7)
    board_boxes = minesweeper_game_board.board_boxes

    for row in range(minesweeper_game_board.rows):
        for col in range(minesweeper_game_board.cols):
            assert isinstance(board_boxes[row][col], MinesweeperBoardBox)


def test_should_not_create_minesweeper_game_board_when_min_rows_is_invalid():
    with pytest.raises(
        ValueError,
        match="Rows and cols values must be greater than 2",
    ):
        MinesweeperGameBoard(2, 10)


def test_should_not_create_minesweeper_game_board_when_min_cols_is_invalid():
    with pytest.raises(
        ValueError,
        match="Rows and cols values must be greater than 2",
    ):
        MinesweeperGameBoard(10, 2)


def test_should_not_create_minesweeper_game_board_when_max_rows_is_invalid():
    with pytest.raises(
        ValueError,
        match="Rows and cols values must be lesser than 18",
    ):
        MinesweeperGameBoard(20, 10)


def test_should_not_create_minesweeper_game_board_when_max_cols_is_invalid():
    with pytest.raises(
        ValueError,
        match="Rows and cols values must be lesser than 18",
    ):
        MinesweeperGameBoard(10, 20)
