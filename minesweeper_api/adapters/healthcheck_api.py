from fastapi import APIRouter

router = APIRouter()


@router.get("/", tags=["healthcheck"])
def healthcheck():
    return {"status": "UP"}
