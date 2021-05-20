from enum import Enum


class GameStatus(Enum):
    INITIALIZED = 1
    IN_PROGRESS = 2
    OVER = 3
    WON = 4
