from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def select_operation():
    return {"message": "Hello, World!"}


@router.post("/")
def insert_operation():
    return {"message": "Hello, World!"}
