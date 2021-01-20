from typing import Optional
from pydantic import BaseModel, EmailStr


class ContactItemBase(BaseModel):
    name: str
    email: EmailStr
    role: Optional[str]
    phone: str


class ContactItemCreate(ContactItemBase):
    public: bool


class ContactItem(ContactItemBase):
    id: int

    class Config:
        orm_mode = True