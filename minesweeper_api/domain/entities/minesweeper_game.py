import uuid
from minesweeper_api.domain.entities.minesweeper_game_board import (
    MinesweeperGameBoard,
)
from enum import Enum


MIN_ROWS_AND_COLS = 3
MAX_ROWS_AND_COLS = 17


class GameStatus(Enum):
    INITIALIZED = 1
    IN_PROGRESS = 2
    OVER = 3
    WON = 4


class MineswpeerGame(object):
    def __init__(self, rows: int, cols: int) -> None:
        self.id = uuid.uuid4()

        if rows < MIN_ROWS_AND_COLS or cols < MIN_ROWS_AND_COLS:
            raise ValueError("Invalid value exception")

        if rows > MAX_ROWS_AND_COLS or cols > MAX_ROWS_AND_COLS:
            raise ValueError("Invalid value exception")

        self.rows = rows
        self.cols = cols
        self.state = GameStatus.INITIALIZED
        self.board = MinesweeperGameBoard(rows, cols)
