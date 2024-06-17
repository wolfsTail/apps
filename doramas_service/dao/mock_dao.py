from doramas_service.dao.abstract_dao import AbstractDAO


class MockDAO(AbstractDAO):
    def __init__(self, data):
        self._data = data

    async def add(self, item):
        self._data.update({len(self._data)+1: item})

    async def all(self):
        return self._data

    async def get(self, item_id):
        return self._data[item_id]

    async def update(self, item_id, item):
        self._data[item_id] = item

    async def delete(self, item_id):
        self._data.pop(item_id)
