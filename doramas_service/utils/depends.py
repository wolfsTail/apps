from fastapi import Depends

from doramas_service.service.doramas_servcie import DoramasService
from doramas_service.service.uow import AbstractUnitOfWork, MockUnitOfWork
from doramas_service.db.FakeDB import DB


async def get_doramas_service_with_mockuow() -> DoramasService:
    uow: AbstractUnitOfWork = MockUnitOfWork(DB)
    return DoramasService(uow)