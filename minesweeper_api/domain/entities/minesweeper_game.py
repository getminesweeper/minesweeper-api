import uuid
from minesweeper_api.domain.entities.minesweeper_game_board import (
    MinesweeperGameBoard,
)
from minesweeper_api.domain.value_objects.game_status import GameStatus


class MineswpeerGame(object):
    def __init__(self, board: MinesweeperGameBoard) -> None:
        self.id = str(uuid.uuid4())
        self.status = GameStatus.INITIALIZED
        self.board = board
