from fastapi import Depends

from doramas_service.service.doramas_servcie import DoramasService
from doramas_service.service.uow import AbstractUnitOfWork, MockUnitOfWork


async def get_doramas_service_with_mockuow(uow: AbstractUnitOfWork = Depends(MockUnitOfWork)) -> DoramasService:
    return DoramasService(uow)