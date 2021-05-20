from minesweeper_api.adapters.rest.rest_minesweeper_game_handler import (
    RestMinesweeperGameHandler,
)
from minesweeper_api.domain.aggregators.minesweeper_game_type import (
    MinesweeperGameType,
)


def test_rest_minesweeper_game_handler_should_create_a_minesweeper_game():
    rest_minesweeper_game_handler = RestMinesweeperGameHandler()
    minesweeper_game_type = MinesweeperGameType(5, 7)
    minesweeper_game = rest_minesweeper_game_handler.add(minesweeper_game_type)

    assert minesweeper_game
    assert minesweeper_game.id
    assert minesweeper_game.rows
    assert minesweeper_game.cols
