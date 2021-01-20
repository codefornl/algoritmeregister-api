from typing import Optional, List
from pydantic import BaseModel, EmailStr
from .contact import ContactItem

class OrganisationItemBase(BaseModel):
    name: str
    department: Optional[str]
    email: Optional[EmailStr]
    phone: Optional[str]
    contacts: Optional[List[ContactItem]]


class OrganisationItemCreate(OrganisationItemBase):
    public: bool


class OrganisationItem(OrganisationItemBase):
    id: int

    class Config:
        orm_mode = True