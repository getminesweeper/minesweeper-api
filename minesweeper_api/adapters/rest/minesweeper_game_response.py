from pydantic import BaseModel
from minesweeper_api.domain.aggregators.minesweeper_game_type import (
    MinesweeperGameType,
)


class MinesweeperGameResponse(BaseModel):
    id: str
    rows: int
    cols: int

    @classmethod
    def from_minesweeper_game_type(
        cls,
        minesweeper_game_type: MinesweeperGameType,
    ):
        return cls(
            id=minesweeper_game_type.id,
            rows=minesweeper_game_type.rows,
            cols=minesweeper_game_type.cols,
        )
