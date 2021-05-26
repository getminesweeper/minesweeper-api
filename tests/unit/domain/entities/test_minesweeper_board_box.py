from minesweeper_api.domain.entities.minesweeper_board_box import (
    MinesweeperBoardBox,
)
from minesweeper_api.domain.value_objects.board_box_status import (
    BoardBoxStatus,
)

import pytest
from minesweeper_api.domain.value_objects.board_box_position import(
    Position,
)


def test_should_create_minesweeper_board_box_when_correct_values_are_given():
    minesweeper_board_box = MinesweeperBoardBox()

    assert minesweeper_board_box.status == BoardBoxStatus.CLOSED
    assert minesweeper_board_box.is_mined is False


def test_should_create_a_correct_position():
    position_row = 0
    position_col = 0

    position = Position(position_row,position_col)

    assert position.position_row == position_row
    assert position.position_col == position_col


def test_should_not_create_the_position_when_row_is_negative():
    position_row = -3
    position_col = 1

    with pytest.raises(
        ValueError,
        match="The minimun value for the row or col position is 0",
    ):
        Position(position_row,position_col)


def test_should_not_create_the_position_when_col_is_negative():
    position_row = 4
    position_col = -5

    with pytest.raises(
        ValueError,
        match="The minimun value for the row or col position is 0",
    ):
        Position(position_row,position_col)