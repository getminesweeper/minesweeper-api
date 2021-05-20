from .minesweeper_board_box import MinesweeperBoardBox


MIN_ROWS_AND_COLS = 3
MAX_ROWS_AND_COLS = 17


class MinesweeperGameBoard(object):
    def __init__(self, rows: int, cols: int) -> None:
        if rows < MIN_ROWS_AND_COLS or cols < MIN_ROWS_AND_COLS:
            raise ValueError(
                "Rows and cols values must be greater than "
                f"{MIN_ROWS_AND_COLS - 1}"
            )

        if rows > MAX_ROWS_AND_COLS or cols > MAX_ROWS_AND_COLS:
            raise ValueError(
                "Rows and cols values must be lesser than "
                f"{MAX_ROWS_AND_COLS + 1}"
            )

        self.board_boxes = [
            [MinesweeperBoardBox()] * cols for _ in range(rows)
        ]

    @property
    def rows(self) -> int:
        return len(self.board_boxes)

    @property
    def cols(self) -> int:
        return len(self.board_boxes[0])
