from schemas.common.crud_response import CRUDResponse

from .common import Response

Create = CRUDResponse[Response]
Read = CRUDResponse[Response]
Update = CRUDResponse[Response]
