from doramas_service.service.uow import AbstractUnitOfWork


class DoramasService:
    def __init__(self, uow: AbstractUnitOfWork):
        self.uow = uow

    async def all(self):
        async with self.uow:
            return await self.uow.doramas.all()

    async def get(self, **kwargs):
        async with self.uow:
            return await self.uow.doramas.get(**kwargs)

    async def create(self, dorama: dict):
        async with self.uow:
            added_model = await self.uow.doramas.add(dorama)
            return added_model

    async def update(self, item_id, item):
        async with self.uow:
            updated_model = await self.uow.doramas.update(item_id, item)
            return updated_model

    async def delete(self, item_id):
        async with self.uow:
            await self.uow.doramas.delete(item_id)
