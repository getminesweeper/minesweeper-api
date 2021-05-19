import pytest
from minesweeper_api.domain.entities.minesweeper_game import (
    MineswpeerGame,
    GameStatus,
)


def test_should_create_minesweeper_game_when_correct_values_are_given():
    minesweeper_game = MineswpeerGame(5, 7)

    assert minesweeper_game.id
    assert minesweeper_game.rows == 5
    assert minesweeper_game.cols == 7
    assert minesweeper_game.state == GameStatus.INITIALIZED
    assert minesweeper_game.board


def test_should_not_create_minesweeper_game_when_min_rows_is_invalid():
    with pytest.raises(
        ValueError,
        match="Invalid value exception",
    ):
        MineswpeerGame(2, 10)


def test_should_not_create_minesweeper_game_when_min_cols_is_invalid():
    with pytest.raises(
        ValueError,
        match="Invalid value exception",
    ):
        MineswpeerGame(10, 2)


def test_should_not_create_minesweeper_game_when_max_rows_is_invalid():
    with pytest.raises(
        ValueError,
        match="Invalid value exception",
    ):
        MineswpeerGame(20, 10)


def test_should_not_create_minesweeper_game_when_max_cols_is_invalid():
    with pytest.raises(
        ValueError,
        match="Invalid value exception",
    ):
        MineswpeerGame(10, 20)
