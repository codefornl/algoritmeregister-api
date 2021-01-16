from typing import List
from fastapi import APIRouter, Depends, Request, HTTPException
from ..schemas import process
from ..config.database import get_db, SessionLocal
from random import randint
from faker import Faker

router = APIRouter()


@router.get("/processes", response_model=List[process.ProcessItem], response_model_exclude_none=True, response_model_by_alias=True)
async def get_processes(limit: int, db: get_db = Depends()):
    fake = Faker()
    result = []
    for x in range(randint(0, limit)):
        result.append(
            process.ProcessItem(
                id=x,
                public=True,
                description=fake.text()
            )
        )
    return result


@router.post("/process", response_model=process.ProcessItem, response_model_exclude_none=True, response_model_by_alias=True)
async def create_process(item: process.ProcessItemCreate, db: get_db = Depends()):
    return process.ProcessItem(
        id=randint(0, 9999),
        public=item.public,
        description=item.description
    )


@router.get("/process/{item_id}", response_model=process.ProcessItem, response_model_exclude_none=True, response_model_by_alias=True)
async def get_process(item_id: int, db: get_db = Depends()):
    fake = Faker()
    return process.ProcessItem(
        id=item_id,
        public=True,
        description=fake.text()
    )
