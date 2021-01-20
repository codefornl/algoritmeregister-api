from typing import List, Optional
from pydantic import BaseModel, HttpUrl, Field
from .organisation import OrganisationItem

class DataItemBase(BaseModel):
    '''
    The data item points to a datasource
    '''
    name: str
    description: str
    license: str
    versions: Optional[List[str]]
    source: HttpUrl # Url pointing to the source code or a webpage describing the model by a vendor
    organisation: OrganisationItem # The organisation that is the source of the datasource
    tags: List[str]


class DataItemCreate(DataItemBase):
    public: bool


class DataItem(DataItemBase):
    id: int

    class Config:
        orm_mode = True