from typing import Optional
from pydantic import BaseModel
from .contact import ContactItem

class OrganisationItemBase(BaseModel):
    name: str
    department: Optional[str]
    contact: ContactItem


class OrganisationItemCreate(OrganisationItemBase):
    public: bool


class OrganisationItem(OrganisationItemBase):
    id: int

    class Config:
        orm_mode = True