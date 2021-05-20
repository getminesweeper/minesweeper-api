from dataclasses import dataclass
from dataclass_type_validator import dataclass_validate


@dataclass_validate
@dataclass(frozen=True)
class MinesweeperGameType:
    rows: int
    cols: int
    id: str = ""
