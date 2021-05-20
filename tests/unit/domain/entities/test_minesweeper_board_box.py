from minesweeper_api.domain.entities.minesweeper_board_box import (
    MinesweeperBoardBox,
)
from minesweeper_api.domain.value_objects.board_box_status import (
    BoardBoxStatus,
)


def test_should_create_minesweeper_board_box_when_correct_values_are_given():
    minesweeper_board_box = MinesweeperBoardBox()

    assert minesweeper_board_box.status == BoardBoxStatus.CLOSED
    assert minesweeper_board_box.is_mined is False
