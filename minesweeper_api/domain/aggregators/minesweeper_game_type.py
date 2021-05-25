from dataclasses import dataclass
from dataclass_type_validator import dataclass_validate
from minesweeper_api.domain.value_objects.game_difficulty import (
    GameDifficulty,
)


@dataclass_validate
@dataclass(frozen=True)
class MinesweeperGameType:
    rows: int
    cols: int
    difficulty: GameDifficulty
    id: str = ""
