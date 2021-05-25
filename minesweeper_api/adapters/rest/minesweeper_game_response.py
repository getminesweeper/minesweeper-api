from pydantic import BaseModel
from minesweeper_api.domain.aggregates.minesweeper_game_type import (
    MinesweeperGameType,
)
from minesweeper_api.domain.value_objects.game_difficulty import (
    GameDifficulty,
)


class MinesweeperGameResponse(BaseModel):
    id: str
    rows: int
    cols: int
    difficulty: GameDifficulty

    @classmethod
    def from_minesweeper_game_type(
        cls,
        minesweeper_game_type: MinesweeperGameType,
    ):
        return cls(
            id=minesweeper_game_type.id,
            rows=minesweeper_game_type.rows,
            cols=minesweeper_game_type.cols,
            difficulty=minesweeper_game_type.difficulty,
        )
