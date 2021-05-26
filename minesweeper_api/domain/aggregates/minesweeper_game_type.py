from dataclasses import dataclass, field
from typing import List
from dataclass_type_validator import dataclass_validate
from minesweeper_api.domain.value_objects.game_difficulty import (
    GameDifficulty,
)

from minesweeper_api.domain.entities.minesweeper_board_box import (
    MinesweeperBoardBox,
)


@dataclass_validate
@dataclass(frozen=True)
class MinesweeperGameType:
    rows: int
    cols: int
    difficulty: GameDifficulty
    board: List[List[MinesweeperBoardBox]] = field(default_factory=list)
    id: str = ""
