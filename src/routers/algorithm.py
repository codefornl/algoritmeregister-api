from typing import List
from fastapi import APIRouter, Depends, Request, HTTPException
from ..schemas import algorithm
from ..config.database import get_db, SessionLocal
from random import randint
from faker import Faker

router = APIRouter()


@router.get("/algorithms", response_model=List[algorithm.AlgorithmItem], response_model_exclude_none=True, response_model_by_alias=True)
async def get_algorithms(limit: int, db: get_db = Depends()):
    fake = Faker()
    result = []
    for x in range(randint(0, limit)):
        result.append(
            algorithm.AlgorithmItem(
                id=x,
                public=True,
                description=fake.text()
            )
        )
    return result


@router.post("/algorithm", response_model=algorithm.AlgorithmItem, response_model_exclude_none=True, response_model_by_alias=True)
async def create_algorithm(item: algorithm.AlgorithmItemCreate, db: get_db = Depends()):
    return algorithm.AlgorithmItem(
        id=randint(0, 9999),
        public=item.public,
        description=item.description
    )


@router.get("/algorithm/{item_id}", response_model=algorithm.AlgorithmItem, response_model_exclude_none=True, response_model_by_alias=True)
async def get_algorithm(item_id: int, db: get_db = Depends()):
    fake = Faker()
    return algorithm.AlgorithmItem(
        id=item_id,
        public=True,
        description=fake.text()
    )
