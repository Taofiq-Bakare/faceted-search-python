"""The models for Standards"""
from typing import Optional
from sqlmodel import Field, SQLModel


class StandardBase(SQLModel):
    catalog_name: str
    catalog_id: str
    topic: str
    sub_topic: str


class Standard(StandardBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class StandardCreate(StandardBase):
    pass


class StandardReturn(Standard):
    catalog_name: str
    catalog_id: str
