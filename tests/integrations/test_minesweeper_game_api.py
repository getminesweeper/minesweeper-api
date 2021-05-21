from fastapi.testclient import TestClient
from fastapi import status
from minesweeper_api.adapters.main_api import app

client = TestClient(app)


def test_should_return_201_create_code_when_payload_is_valid():
    request = {
        "rows": 7,
        "cols": 8,
    }
    response = client.post("/api/games/", json=request)

    assert status.HTTP_201_CREATED == response.status_code
    assert response.json()["rows"]
    assert request["rows"] == response.json()["rows"]
    assert request["cols"] == response.json()["cols"]


def test_should_return_400_bad_request_when_min_rows_is_invalid():
    request = {
        "rows": 2,
        "cols": 8,
    }
    response = client.post("/api/games/", json=request)

    assert status.HTTP_400_BAD_REQUEST == response.status_code
    assert (
        "The minimum amount of rows and cols to be configured is 3"
        == response.json()["detail"]
    )


def test_should_return_400_bad_request_when_min_cols_is_invalid():
    request = {
        "rows": 8,
        "cols": 2,
    }
    response = client.post("/api/games/", json=request)

    assert status.HTTP_400_BAD_REQUEST == response.status_code
    assert (
        "The minimum amount of rows and cols to be configured is 3"
        == response.json()["detail"]
    )


def test_should_return_400_bad_request_when_max_rows_is_invalid():
    request = {
        "rows": 20,
        "cols": 8,
    }
    response = client.post("/api/games/", json=request)

    assert status.HTTP_400_BAD_REQUEST == response.status_code
    assert (
        "The maximum amount of rows and cols to be configured is 17"
        == response.json()["detail"]
    )


def test_should_return_400_bad_request_when_max_cols_is_invalid():
    request = {
        "rows": 8,
        "cols": 20,
    }
    response = client.post("/api/games/", json=request)

    assert status.HTTP_400_BAD_REQUEST == response.status_code
    assert (
        "The maximum amount of rows and cols to be configured is 17"
        == response.json()["detail"]
    )


def test_should_return_422_status_code_when_rows_and_cols_are_not_integers():
    request = {
        "rows": 8.5,
        "cols": 4.5,
    }
    response = client.post("/api/games/", json=request)

    assert status.HTTP_422_UNPROCESSABLE_ENTITY == response.status_code
