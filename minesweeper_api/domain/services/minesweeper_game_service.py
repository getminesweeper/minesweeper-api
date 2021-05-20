from minesweeper_api.domain.entities.minesweeper_game import MineswpeerGame
from minesweeper_api.domain.entities.minesweeper_game_board import (
    MinesweeperGameBoard,
)


class MinesweeperGameService:
    def __init__(self) -> None:
        super().__init__()

    def create(self, rows: int, cols: int) -> MineswpeerGame:
        minesweeper_game_board = MinesweeperGameBoard(rows, cols)
        minesweeper_game = MineswpeerGame(minesweeper_game_board)
        return minesweeper_game
