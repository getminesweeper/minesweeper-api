from pydantic import BaseModel
from minesweeper_api.domain.aggregators.minesweeper_game_type import (
    MinesweeperGameType,
)


class MinesweeperGameRequest(BaseModel):
    rows: int
    cols: int

    def get_minesweeper_game_type(self):
        return MinesweeperGameType(self.rows, self.cols)
