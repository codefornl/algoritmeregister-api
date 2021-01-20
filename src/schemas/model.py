from typing import List, Optional
from pydantic import BaseModel, HttpUrl, Field
from .organisation import OrganisationItem

class ModelItemBase(BaseModel):
    '''
    The model is the part of the algorithm that generates output from data by performing
    given steps
    '''
    name: str
    description: str
    model_type: str = Field(...,alias='type')
    source: HttpUrl # Url pointing to the source code or a webpage describing the model by a vendor
    output: Optional[HttpUrl]
    tags: List[str]
    models: Optional[HttpUrl] # Url's to images containing model diagrams
    organisation: Optional[OrganisationItem] # Organisation intellectually owning the model

class ModelItemCreate(ModelItemBase):
    public: bool


class ModelItem(ModelItemBase):
    id: int

    class Config:
        orm_mode = True