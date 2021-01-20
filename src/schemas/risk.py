from typing import List, Optional
from pydantic import BaseModel, HttpUrl, Field
from .organisation import OrganisationItem

class RiskItemBase(BaseModel):
    '''
    Risk according to general risk model techniques
    '''
    name: str
    description: str
    probability: ProbabilityItem
    severity: SeverityItem


class RiskItemCreate(RiskItemBase):
    public: bool


class RiskItem(RiskItemBase):
    id: int

    class Config:
        orm_mode = True