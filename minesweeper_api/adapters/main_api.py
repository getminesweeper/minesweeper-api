import uvicorn
from fastapi import FastAPI
from minesweeper_api.adapters.rest import minesweeper_game_api
from minesweeper_api.adapters import healthcheck_api

REST_API_HOST = "0.0.0.0"
REST_API_PORT = 8000

app = FastAPI()
app.include_router(minesweeper_game_api.router)
app.include_router(healthcheck_api.router)


def run():
    uvicorn.run(
        "minesweeper_api.adapters.main_api:app",
        host=REST_API_HOST,
        port=REST_API_PORT,
        reload=True,
    )
