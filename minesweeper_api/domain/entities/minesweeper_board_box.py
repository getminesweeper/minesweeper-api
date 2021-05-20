from minesweeper_api.domain.value_objects.board_box_status import (
    BoardBoxStatus,
)


class MinesweeperBoardBox(object):
    def __init__(self) -> None:
        self.status = BoardBoxStatus.CLOSED
        self.is_mined = False
