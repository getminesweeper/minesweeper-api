from minesweeper_api.domain.entities.minesweeper_game_board import (
    MinesweeperGameBoard,
)
from minesweeper_api.domain.entities.minesweeper_board_box import (
    MinesweeperBoardBox,
)


def test_should_create_minesweeper_game_board_when_correct_values_are_given():
    minesweeper_game_board = MinesweeperGameBoard(5, 7)

    assert minesweeper_game_board.board_boxes
    assert len(minesweeper_game_board.board_boxes) == 5
    assert len(minesweeper_game_board.board_boxes[0]) == 7


def test_board_boxes_should_be_instance_of_board_box():
    minesweeper_game_board = MinesweeperGameBoard(5, 7)
    board_boxes = minesweeper_game_board.board_boxes

    for row in range(len(board_boxes)):
        for col in range(len(board_boxes[0])):
            assert isinstance(board_boxes[row][col], MinesweeperBoardBox)
