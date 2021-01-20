from typing import List, Optional
from pydantic import BaseModel, HttpUrl, Field
from .risk import RiskItem

class SeverityItemBase(BaseModel):
    '''
    Severity according to general risk model techniques
    '''
    name: str
    description: str
    value: int


class SeverityItemCreate(SeverityItemBase):
    public: bool


class SeverityItem(SeverityItemBase):
    id: int

    class Config:
        orm_mode = True