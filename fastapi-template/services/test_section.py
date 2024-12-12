from schemas.test_section import bodies, params, responses


class TestSectionService:
    def __init__(self):
        pass

    async def create(
        self,
        params: params.Create,
        body: bodies.Create
    ) -> responses.Create:
        ...

    async def read(
        self,
        params: params.Read,
        body: bodies.Read
    ) -> responses.Read:
        ...

    async def update(
        self,
        params: params.Create,
        body: bodies.Create
    ) -> responses.Create:
        ...

    async def delete(
        self,
        params: params.Delete,
        body: bodies.Delete
    ) -> responses.Delete:
        ...
