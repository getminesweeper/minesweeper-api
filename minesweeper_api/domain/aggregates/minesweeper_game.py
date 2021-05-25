import uuid
from minesweeper_api.domain.entities.minesweeper_game_board import (
    MinesweeperGameBoard,
)
from minesweeper_api.domain.value_objects.game_status import GameStatus
from minesweeper_api.domain.value_objects.game_difficulty import GameDifficulty


class MineswpeerGame(object):
    def __init__(
        self, board: MinesweeperGameBoard, difficulty: GameDifficulty
    ) -> None:
        self.id = str(uuid.uuid4())
        self.status = GameStatus.INITIALIZED
        self.board = board
        self.difficulty = difficulty
