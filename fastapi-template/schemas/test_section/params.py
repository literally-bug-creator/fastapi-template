from fastapi import Path
from pydantic import BaseModel


class Create(BaseModel):
    id: int = Path()


class Read(BaseModel):
    id: int = Path()


class Update(BaseModel):
    id: int = Path()


class Delete(BaseModel):
    id: int = Path()
