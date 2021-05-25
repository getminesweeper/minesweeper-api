from minesweeper_api.domain_ports.minesweeper_game_handler import (
    MinesweeperGameHandler,
)
from minesweeper_api.domain.aggregates.minesweeper_game_type import (
    MinesweeperGameType,
)
from minesweeper_api.adapters.rest.minesweeper_game_response import (
    MinesweeperGameResponse,
)
from minesweeper_api.adapters.repositories.memory_minesweeper_game_repository import (
    MemoryMinesweeperGameRepository,
)
from minesweeper_api.domain.entities.minesweeper_game import (
    MineswpeerGame,
)


class RestMinesweeperGameHandler(MinesweeperGameHandler):
    def __init__(self) -> None:
        self.minesweeper_game_repository = MemoryMinesweeperGameRepository()

    def add(
        self, minesweeper_game_type: MinesweeperGameType
    ) -> MineswpeerGame:
        minesweeper_game = self.minesweeper_game_repository.add(
            minesweeper_game_type
        )
        return MinesweeperGameResponse.from_minesweeper_game_type(
            minesweeper_game
        )
