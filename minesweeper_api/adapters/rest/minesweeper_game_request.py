from pydantic import BaseModel, StrictInt
from minesweeper_api.domain.aggregators.minesweeper_game_type import (
    MinesweeperGameType,
)
from minesweeper_api.domain.value_objects.game_difficulty import (
    GameDifficulty,
)


class MinesweeperGameRequest(BaseModel):
    rows: StrictInt
    cols: StrictInt
    difficulty: GameDifficulty

    def get_minesweeper_game_type(self):
        return MinesweeperGameType(self.rows, self.cols, self.difficulty)
