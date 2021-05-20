from minesweeper_api.domain_ports.minesweeper_game_repository import (
    MinesweeperGameRepository,
)
from minesweeper_api.domain.aggregators.minesweeper_game_type import (
    MinesweeperGameType,
)
from minesweeper_api.domain.services.minesweeper_game_service import (
    MinesweeperGameService,
)
from minesweeper_api.domain.entities.minesweeper_game import (
    MineswpeerGame,
)


def _map_to_minesweeper_game_type(minesweeper_game: MineswpeerGame):
    minesweeper_game_type = None
    if minesweeper_game:
        minesweeper_game_type = MinesweeperGameType(
            id=minesweeper_game.id,
            rows=minesweeper_game.board.rows,
            cols=minesweeper_game.board.cols,
        )
    return minesweeper_game_type


class MemoryMinesweeperGameRepository(MinesweeperGameRepository):
    def __init__(self) -> None:
        self.minesweeper_game_data = dict()
        self.minesweeper_game_service = MinesweeperGameService()

    def add(
        self, minesweeper_game_type: MinesweeperGameType
    ) -> MinesweeperGameType:
        try:
            minesweeper_game = self.minesweeper_game_service.create(
                minesweeper_game_type.rows, minesweeper_game_type.cols
            )
            self.minesweeper_game_data[minesweeper_game.id] = minesweeper_game
            return _map_to_minesweeper_game_type(minesweeper_game)
        except Exception as e:
            raise e
