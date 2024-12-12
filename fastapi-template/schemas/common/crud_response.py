from pydantic import BaseModel


class CRUDResponse[T](BaseModel):
    item: T
