from pydantic import BaseModel


class OrganisationItemBase(BaseModel):
    description: str


class OrganisationItemCreate(OrganisationItemBase):
    public: bool


class OrganisationItem(OrganisationItemBase):
    id: int

    class Config:
        orm_mode = True