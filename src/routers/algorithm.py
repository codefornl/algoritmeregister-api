from fastapi import APIRouter, Depends, Request, HTTPException
from ..schemas import algorithm
from ..config.database import get_db, SessionLocal

router = APIRouter()

# Dependency
def get_db(request: Request):
    return request.state.db


@router.post("/algorithm/")
async def create_item(item:algorithm.AlgorithmItemCreate, db: get_db = Depends()):
    return "ok"


@router.get("/algorithm/{item_id}")
async def get_algorithm(item_id: int, db: get_db = Depends()):
    return "ok"
    