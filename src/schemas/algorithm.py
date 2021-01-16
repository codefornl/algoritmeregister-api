from pydantic import BaseModel


class AlgorithmItemBase(BaseModel):
    description: str


class AlgorithmItemCreate(AlgorithmItemBase):
    public: bool


class AlgorithmItem(AlgorithmItemBase):
    id: int

    class Config:
        orm_mode = True