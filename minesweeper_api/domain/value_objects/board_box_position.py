MIN_POSITION = 0

class Position ():
    position_row: int
    position_col: int

    def __init__(self, row: int, col: int) -> None:
        if row < MIN_POSITION or col < MIN_POSITION:
            raise ValueError(
                "The minimun value for the row or col position"
                f" is {MIN_POSITION}"
            )
        self.position_row = row
        self.position_col = col
