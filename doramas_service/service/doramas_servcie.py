from doramas_service.service.uow import AbstractUnitOfWork


class DoramasService:
    def __init__(self, uow: AbstractUnitOfWork):
        self.uow = uow

    async def all(self):
        async with self.uow:
            return await self.uow.doramas.all()

    async def get(self, **kwargs):
        async with self.uow:
            return await self.uow.doramas.get(kwargs["id"]) if kwargs["id"] else await self.uow.doramas.get(**kwargs)

    async def create(self):
        pass

    async def update(self):
        pass

    async def delete(self):
        pass
