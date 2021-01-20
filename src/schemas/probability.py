from typing import List, Optional
from pydantic import BaseModel, HttpUrl, Field
from .risk import RiskItem

class ProbabilityItemBase(BaseModel):
    '''
    Probability according to general risk model techniques
    '''
    name: str
    description: str
    value: int


class ProbabilityItemCreate(ProbabilityItemBase):
    public: bool


class ProbabilityItem(ProbabilityItemBase):
    id: int

    class Config:
        orm_mode = True