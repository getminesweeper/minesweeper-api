from minesweeper_api.adapters.rest.rest_minesweeper_game_handler import (
    RestMinesweeperGameHandler,
)
from minesweeper_api.domain.aggregates.minesweeper_game_type import (
    MinesweeperGameType,
)
from minesweeper_api.domain.value_objects.game_difficulty import (
    GameDifficulty,
)


def test_rest_minesweeper_game_handler_should_create_a_minesweeper_game():
    rest_minesweeper_game_handler = RestMinesweeperGameHandler()
    minesweeper_game_type = MinesweeperGameType(5, 7, GameDifficulty.EASY)
    minesweeper_game = rest_minesweeper_game_handler.add(minesweeper_game_type)

    assert minesweeper_game
    assert minesweeper_game.id
    assert minesweeper_game.rows == 5
    assert minesweeper_game.cols == 7
    assert minesweeper_game.difficulty == GameDifficulty.EASY
