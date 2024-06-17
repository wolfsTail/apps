import pytest

from doramas_service.service import DoramasService
from doramas_service.service.uow import MockUnitOfWork
from doramas_service.dao import MockDAO


@pytest.mark.asyncio
async def test_get_all_doramas_from_service():
    data = {
        1: {"id": 1, "name": "Doramas 1"},
        2: {"id": 2, "name": "Doramas 2"},
        3: {"id": 3, "name": "Doramas 3"},
    }
    uow = MockUnitOfWork(data)
    service = DoramasService(uow)
    result = await service.all()
    print(result)
    assert result == data
    