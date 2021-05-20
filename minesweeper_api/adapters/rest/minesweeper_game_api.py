from fastapi import APIRouter, status
from minesweeper_api.adapters.rest.minesweeper_game_response import (
    MinesweeperGameResponse,
)
from minesweeper_api.adapters.rest.minesweeper_game_request import (
    MinesweeperGameRequest,
)
from minesweeper_api.domain_ports.minesweeper_game_handler import (
    MinesweeperGameHandler,
)

router = APIRouter()


@router.post(
    "/api/games/",
    tags=["minesweeper-game"],
    status_code=status.HTTP_201_CREATED,
    response_model=MinesweeperGameResponse,
)
def create_minesweeper_game(minesweeper_game_input: MinesweeperGameRequest):
    try:
        minesweeper_game_handler = MinesweeperGameHandler()
        created_minesweeper_game = minesweeper_game_handler.create(
            minesweeper_game_input.get_minesweeper_game_type()
        )
        return created_minesweeper_game
    except Exception as exception:
        raise exception
