from minesweeper_api.domain.aggregates.minesweeper_game import MineswpeerGame
from minesweeper_api.domain.entities.minesweeper_game_board import (
    MinesweeperGameBoard,
)
from minesweeper_api.domain.value_objects.game_difficulty import (
    GameDifficulty,
)


class MinesweeperGameService:
    def __init__(self) -> None:
        super().__init__()

    def create(
        self, rows: int, cols: int, difficulty: GameDifficulty
    ) -> MineswpeerGame:
        minesweeper_game_board = MinesweeperGameBoard(rows, cols, difficulty)
        minesweeper_game = MineswpeerGame(minesweeper_game_board, difficulty)
        return minesweeper_game
