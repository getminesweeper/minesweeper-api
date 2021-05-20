from minesweeper_api.domain.entities.minesweeper_game import (
    MineswpeerGame,
)
from minesweeper_api.domain.value_objects.game_status import GameStatus
from minesweeper_api.domain.entities.minesweeper_game_board import (
    MinesweeperGameBoard,
)


def test_should_create_minesweeper_game_when_correct_values_are_given():
    minesweeper_game_box = MinesweeperGameBoard(5, 7)
    minesweeper_game = MineswpeerGame(minesweeper_game_box)

    assert minesweeper_game.id
    assert minesweeper_game.status == GameStatus.INITIALIZED
    assert minesweeper_game.board
