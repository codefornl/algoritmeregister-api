from sqlalchemy import Boolean, Column, Integer, String

from config.database import Base


class Algorithm(Base):
    __tablename__ = "algorithms"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    public = Column(Boolean, default=False)