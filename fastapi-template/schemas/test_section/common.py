from pydantic import BaseModel


class Response(BaseModel):
    id: int
    value: int
