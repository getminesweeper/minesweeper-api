from minesweeper_api.domain_ports.minesweeper_game_handler import (
    MinesweeperGameHandler,
)
from minesweeper_api.domain.aggregators.minesweeper_game_type import (
    MinesweeperGameType,
)
from minesweeper_api.domain.services.minesweeper_game_service import (
    MinesweeperGameService,
)


class RestMinesweeperGameHandler(MinesweeperGameHandler):
    def __init__(self) -> None:
        self.minesweeper_game_service = MinesweeperGameService()

    def add(self, minesweeper_game_type: MinesweeperGameType):
        minesweeper_game = self.minesweeper_game_service.create(
            minesweeper_game_type.rows, minesweeper_game_type.cols
        )
        return minesweeper_game
