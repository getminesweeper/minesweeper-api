from fastapi import APIRouter, status
from minesweeper_api.adapters.rest.minesweeper_game_response import (
    MinesweeperGameResponse,
)
from minesweeper_api.adapters.rest.minesweeper_game_request import (
    MinesweeperGameRequest,
)
from minesweeper_api.adapters.rest.rest_minesweeper_game_handler import (
    RestMinesweeperGameHandler,
)
from minesweeper_api.adapters.rest.error_validations import (
    handle_minesweeper_api_exceptions,
)


router = APIRouter()
minesweeper_game_handler = RestMinesweeperGameHandler()


@router.post(
    "/api/games/",
    tags=["minesweeper-game"],
    status_code=status.HTTP_201_CREATED,
    response_model=MinesweeperGameResponse,
)
def create_minesweeper_game(minesweeper_game_input: MinesweeperGameRequest):
    try:
        created_minesweeper_game = minesweeper_game_handler.add(
            minesweeper_game_input.get_minesweeper_game_type()
        )
        return created_minesweeper_game
    except Exception as exception:
        handle_minesweeper_api_exceptions(exception)
