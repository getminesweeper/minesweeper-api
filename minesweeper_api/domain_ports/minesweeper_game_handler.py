from abc import ABC, abstractmethod
from minesweeper_api.domain.aggregates.minesweeper_game_type import (
    MinesweeperGameType,
)
from minesweeper_api.domain.entities.minesweeper_game import (
    MineswpeerGame,
)


class MinesweeperGameHandler(ABC):
    @abstractmethod
    def add(
        self, minesweeper_game_type: MinesweeperGameType
    ) -> MineswpeerGame:
        pass
