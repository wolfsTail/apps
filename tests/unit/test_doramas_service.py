import pytest

from doramas_service.service import DoramasService
from doramas_service.service.uow import MockUnitOfWork


data = {
        1: {"id": 1, "name": "Doramas 1"},
        2: {"id": 2, "name": "Doramas 2"},
        3: {"id": 3, "name": "Doramas 3"},
    }

def create_service(data):
    uow = MockUnitOfWork(data)
    service = DoramasService(uow)
    return service

@pytest.mark.asyncio
async def test_get_all_doramas_from_service():
    service = create_service(data)
    result = await service.all()
    assert result == data

@pytest.mark.asyncio
async def test_get_dorama_from_service():
    service = create_service(data)
    result = await service.get(id=1)
    assert result == data[1]

@pytest.mark.asyncio
async def test_add_one_dorama():
    service = create_service(data)
    result = await service.create({"name": "Doramas 4"})
    assert result["name"] == "Doramas 4"
    assert result["id"] == 4
