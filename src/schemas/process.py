from pydantic import BaseModel


class ProcessItemBase(BaseModel):
    description: str


class ProcessItemCreate(ProcessItemBase):
    public: bool


class ProcessItem(ProcessItemBase):
    id: int

    class Config:
        orm_mode = True