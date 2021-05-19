from .minesweeper_board_box import MinesweeperBoardBox


class MinesweeperGameBoard(object):
    def __init__(self, rows: int, cols: int) -> None:
        self.board_boxes = [[MinesweeperBoardBox()] * cols for i in range(rows)]
