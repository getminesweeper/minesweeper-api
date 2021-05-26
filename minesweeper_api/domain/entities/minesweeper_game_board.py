import random
from .minesweeper_board_box import MinesweeperBoardBox
from minesweeper_api.domain.value_objects.game_difficulty import (
    GameDifficulty,
)

MIN_ROWS_AND_COLS = 3
MAX_ROWS_AND_COLS = 17
MINES_PERCENTAGE_EASY = 10
MINES_PERCENTAGE_MEDIUM = 50
MINES_PERCENTAGE_HARD = 75


class MinesweeperGameBoard(object):
    def __init__(
        self, rows: int, cols: int, difficulty: GameDifficulty
    ) -> None:
        if rows < MIN_ROWS_AND_COLS or cols < MIN_ROWS_AND_COLS:
            raise ValueError(
                "The minimum amount of rows and cols to be "
                f"configured is {MIN_ROWS_AND_COLS}"
            )

        if rows > MAX_ROWS_AND_COLS or cols > MAX_ROWS_AND_COLS:
            raise ValueError(
                "The maximum amount of rows and cols to be "
                f"configured is {MAX_ROWS_AND_COLS}"
            )

        self.board_boxes = []
        for row in range(rows):
            self.board_boxes.append([])
            for _ in range(cols):
                self.board_boxes[row].append(MinesweeperBoardBox())

        self.amount_of_mines = self.__calculate_amount_of_mines(difficulty)
        self.__assign_mines()

    @property
    def rows(self) -> int:
        return len(self.board_boxes)

    @property
    def cols(self) -> int:
        return len(self.board_boxes[0])

    def __calculate_amount_of_mines(self, difficulty: GameDifficulty) -> int:
        difficulties = {
            GameDifficulty.EASY: MINES_PERCENTAGE_EASY,
            GameDifficulty.MEDIUM: MINES_PERCENTAGE_MEDIUM,
            GameDifficulty.HARD: MINES_PERCENTAGE_HARD,
        }
        mines_percent = difficulties.get(difficulty) / 100.0

        return round(self.rows * self.cols * mines_percent)

    def __assign_mines(self):
        assigned_mines = 0

        while assigned_mines < self.amount_of_mines:
            row = random.randint(0, self.rows - 1)
            col = random.randint(0, self.cols - 1)

            if not self.board_boxes[row][col].is_mined:
                self.board_boxes[row][col].is_mined = True
                assigned_mines += 1
