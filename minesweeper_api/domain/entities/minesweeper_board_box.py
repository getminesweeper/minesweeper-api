from enum import Enum


class BoardBoxStatus(Enum):
    CLOSED = 1
    OPENED = 2
    FLAGGED = 3


class MinesweeperBoardBox(object):
    def __init__(self) -> None:
        self.status = BoardBoxStatus.CLOSED
        self.is_mined = False
