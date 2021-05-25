from abc import ABC, abstractmethod
from minesweeper_api.domain.aggregates.minesweeper_game_type import (
    MinesweeperGameType,
)


class MinesweeperGameRepository(ABC):
    @abstractmethod
    def add(
        self, minesweeper_game_type: MinesweeperGameType
    ) -> MinesweeperGameType:
        pass
