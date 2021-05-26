from pydantic import BaseModel
from typing import List

from minesweeper_api.domain.aggregates.minesweeper_game_type import (
    MinesweeperGameType,
)
from minesweeper_api.domain.value_objects.game_difficulty import (
    GameDifficulty,
)

from minesweeper_api.domain.value_objects.board_box_status import (
    BoardBoxStatus,
)


class BoardBox(BaseModel):
    status: BoardBoxStatus
    is_mined: bool


class MinesweeperGameResponse(BaseModel):
    id: str
    rows: int
    cols: int
    difficulty: GameDifficulty
    board: List[List[BoardBox]]

    @classmethod
    def from_minesweeper_game_type(
        cls,
        minesweeper_game_type: MinesweeperGameType,
    ):


        board_boxes = []
        for row in minesweeper_game_type.board:
            board_boxes.append(
                [
                    BoardBox(status=box.status, is_mined=box.is_mined)
                    for box in row
                ]
            )
        return cls(
            id=minesweeper_game_type.id,
            rows=minesweeper_game_type.rows,
            cols=minesweeper_game_type.cols,
            difficulty=minesweeper_game_type.difficulty,
            board=board_boxes,
        )
