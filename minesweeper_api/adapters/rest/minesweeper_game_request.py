from pydantic import BaseModel, StrictInt
from minesweeper_api.domain.aggregators.minesweeper_game_type import (
    MinesweeperGameType,
)


class MinesweeperGameRequest(BaseModel):
    rows: StrictInt
    cols: StrictInt

    def get_minesweeper_game_type(self):
        return MinesweeperGameType(self.rows, self.cols)
