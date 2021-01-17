from typing import List
from pydantic import BaseModel, HttpUrl
from .organisation import OrganisationItem

class AlgorithmItemBase(BaseModel):
    name: str
    description: str
    link: HttpUrl
    tags: List[str]
    organisation: OrganisationItem

class AlgorithmItemCreate(AlgorithmItemBase):
    public: bool


class AlgorithmItem(AlgorithmItemBase):
    id: int

    class Config:
        orm_mode = True