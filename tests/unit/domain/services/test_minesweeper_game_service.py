from minesweeper_api.domain.services.minesweeper_game_service import (
    MinesweeperGameService,
)
from minesweeper_api.domain.value_objects.game_status import GameStatus
from minesweeper_api.domain.value_objects.game_difficulty import (
    GameDifficulty,
)


def test_should_create_minesweeper_game_service_with_correct_values():
    minesweeper_game_service = MinesweeperGameService()
    minesweeper_game = minesweeper_game_service.create(
        5, 7, GameDifficulty.EASY
    )

    assert minesweeper_game
    assert minesweeper_game.status == GameStatus.INITIALIZED
    assert minesweeper_game.id
    assert minesweeper_game.board
    assert minesweeper_game.difficulty == GameDifficulty.EASY
