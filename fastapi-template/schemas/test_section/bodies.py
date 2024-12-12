from pydantic import BaseModel


class Create(BaseModel):
    value: int


class Read(BaseModel):
    ...


class Update(BaseModel):
    value: int


class Delete(BaseModel):
    ...
