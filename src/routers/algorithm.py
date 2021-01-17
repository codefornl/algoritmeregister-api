from typing import List
from fastapi import APIRouter, Depends, Request, HTTPException
from ..schemas import algorithm, contact, organisation
from ..config.database import get_db, SessionLocal
from random import randint
from faker import Faker

router = APIRouter()


@router.get("/algorithms", response_model=List[algorithm.AlgorithmItem], response_model_exclude_none=True, response_model_by_alias=True)
async def get_algorithms(limit: int, db: get_db = Depends()):
    fake = Faker()
    result = []
    tags = []
    for _ in range(randint(0, 10)):
        tags.append(fake.word())
    for x in range(randint(0, limit)):
        tags = []
        for _ in range(randint(0, 10)):
            tags.append(fake.word())

        c = contact.ContactItem(
            id=randint(0, 9999),
            name=fake.name_nonbinary(),
            email=fake.email(),
            phone=fake.phone_number(),
            public=True,
        )

        o = organisation.OrganisationItem(
            id=randint(0, 9999),
            name=fake.company(),
            department=fake.word(),
            contact=c
        )
        result.append(
            algorithm.AlgorithmItem(
                id=x,
                name=fake.first_name_nonbinary(),
                public=True,
                description=fake.text(),
                link=fake.uri(),
                tags=tags,
                organisation=o
            )
        )
    return result


@router.post("/algorithm", response_model=algorithm.AlgorithmItem, response_model_exclude_none=True, response_model_by_alias=True)
async def create_algorithm(item: algorithm.AlgorithmItemCreate, db: get_db = Depends()):
    return algorithm.AlgorithmItem(
        id=randint(0, 9999),
        name=item.name,
        public=item.public,
        description=item.description,
        link=item.link,
        tags=item.tags,
        organisation=item.organisation
    )


@router.get("/algorithm/{item_id}", response_model=algorithm.AlgorithmItem, response_model_exclude_none=True, response_model_by_alias=True)
async def get_algorithm(item_id: int, db: get_db = Depends()):
    fake = Faker()
    tags = []
    c = contact.ContactItem(
        id=randint(0, 9999),
        name=fake.name_nonbinary(),
        email=fake.email(),
        phone=fake.phone_number(),
        public=True,
    )

    o = organisation.OrganisationItem(
        id=randint(0, 9999),
        name=fake.company(),
        department=fake.word(),
        contact=c
    )

    for _ in range(randint(0, 10)):
        tags.append(fake.word())
    return algorithm.AlgorithmItem(
        id=item_id,
        name=fake.first_name_nonbinary(),
        public=True,
        description=fake.text(),
        link=fake.uri(),
        tags=tags,
        organisation=o
    )
