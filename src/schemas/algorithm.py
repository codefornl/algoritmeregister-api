from typing import List, Optional
from pydantic import BaseModel, HttpUrl, Field
from .organisation import OrganisationItem

class AlgorithmItemBase(BaseModel):
    name: str
    description: str
    algorithm_type: str = Field(...,alias='type')
    link: HttpUrl
    tags: List[str]
    organisation: OrganisationItem
    auditor: Optional[OrganisationItem]
    vendor: Optional[OrganisationItem]

class AlgorithmItemCreate(AlgorithmItemBase):
    public: bool


class AlgorithmItem(AlgorithmItemBase):
    id: int

    class Config:
        orm_mode = True