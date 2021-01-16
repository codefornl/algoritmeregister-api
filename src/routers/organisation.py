from typing import List
from fastapi import APIRouter, Depends, Request, HTTPException
from ..schemas import organisation
from ..config.database import get_db, SessionLocal
from random import randint
from faker import Faker

router = APIRouter()


@router.get("/organisations", response_model=List[organisation.OrganisationItem], response_model_exclude_none=True, response_model_by_alias=True)
async def get_organisations(limit: int, db: get_db = Depends()):
    fake = Faker()
    result = []
    for x in range(randint(0, limit)):
        result.append(
            organisation.OrganisationItem(
                id=x,
                public=True,
                description=fake.text()
            )
        )
    return result


@router.post("/organisation", response_model=organisation.OrganisationItem, response_model_exclude_none=True, response_model_by_alias=True)
async def create_organisation(item: organisation.OrganisationItemCreate, db: get_db = Depends()):
    return organisation.OrganisationItem(
        id=randint(0, 9999),
        public=item.public,
        description=item.description
    )


@router.get("/organisation/{item_id}", response_model=organisation.OrganisationItem, response_model_exclude_none=True, response_model_by_alias=True)
async def get_organisation(item_id: int, db: get_db = Depends()):
    fake = Faker()
    return organisation.OrganisationItem(
        id=item_id,
        public=True,
        description=fake.text()
    )
