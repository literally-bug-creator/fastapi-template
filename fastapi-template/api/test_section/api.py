from fastapi import APIRouter, Depends, status
from schemas.test_section import bodies, params, responses
from services.test_section import TestSectionService

from .settings import PREFIX, Path

router = APIRouter(prefix=PREFIX)


@router.put(
    path=Path.CREATE,
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_201_CREATED: {"model": responses.Create},
    },
    description="CREATE endpoint",
)
async def create(
    params: params.Create = Depends(),
    body: bodies.Create = Depends(),
    service: TestSectionService = Depends(),
):
    return await service.create(params, body)


@router.get(
    path=Path.READ,
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_200_OK: {"model": responses.Create},
    },
    description="READ endpoint",
)
async def read(
    params: params.Read = Depends(),
    body: bodies.Read = Depends(),
    service: TestSectionService = Depends(),
):
    return await service.read(params, body)


@router.patch(
    path=Path.UPDATE,
    status_code=status.HTTP,
    responses={
        status.HTTP_200_OK: {"model": responses.Update},
    },
    description="UPDATE endpoint",
)
async def update(
    params: params.Update = Depends(),
    body: bodies.Update = Depends(),
    service: TestSectionService = Depends(),
):
    return await service.update(params, body)


@router.delete(
    path=Path.DELETE,
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        status.HTTP_204_NO_CONTENT: {"model": responses.Delete},
    },
    description="DELETE endpoint",
)
async def delete(
    params: params.Delete = Depends(),
    body: bodies.Delete = Depends(),
    service: TestSectionService = Depends(),
):
    return await service.delete(params, body)
