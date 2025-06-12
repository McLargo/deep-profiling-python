from pydantic import BaseModel


class Item(BaseModel):
    key: str
    value: str


class ItemKey(BaseModel):
    key: str
