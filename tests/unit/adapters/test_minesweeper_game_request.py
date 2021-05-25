from minesweeper_api.adapters.rest.minesweeper_game_request import (
    MinesweeperGameRequest,
)
from minesweeper_api.domain.aggregators.minesweeper_game_type import (
    MinesweeperGameType,
)


def test_should_return_minesweeper_game_type_given_minesweeper_game_request():
    minesweeper_game_request = MinesweeperGameRequest(
        rows=5, cols=7, difficulty="EASY"
    )
    minesweeper_game_type = (
        minesweeper_game_request.get_minesweeper_game_type()
    )

    assert isinstance(minesweeper_game_type, MinesweeperGameType)
    assert minesweeper_game_type.rows == 5
    assert minesweeper_game_type.cols == 7
    assert minesweeper_game_type.difficulty == "EASY"
