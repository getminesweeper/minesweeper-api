from fastapi import status, HTTPException


def handle_minesweeper_api_exceptions(exception: Exception):
    error_message = str(exception)
    if isinstance(exception, ValueError):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=error_message
        ) from exception

    raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail="Unexpected error.",
    ) from exception
