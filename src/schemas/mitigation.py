from typing import List, Optional
from pydantic import BaseModel, HttpUrl, Field
from .risk import RiskItem

class MitigationItemBase(BaseModel):
    '''
    Mitigation according to general risk model techniques
    '''
    name: str
    description: str
    risk: Risk # the risk the mitigation belongs to



class MitigationItemCreate(MitigationItemBase):
    public: bool


class MitigationItem(MitigationItemBase):
    id: int

    class Config:
        orm_mode = True