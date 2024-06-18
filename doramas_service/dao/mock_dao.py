from doramas_service.dao.abstract_dao import AbstractDAO


class MockDAO(AbstractDAO):
    def __init__(self, data):
        self._data = data

    async def add(self, item):
        item_id = len(self._data) + 1
        item["id"] = item_id
        self._data.update({item_id: item})
        return self._data[item_id]

    async def all(self):
        return self._data

    async def get(self, **kwargs):
        if "id" in kwargs:
            item_id = kwargs["id"]
            return self._data[item_id]

    async def update(self, item_id, item):
        self._data[item_id] = item

    async def delete(self, item_id):
        self._data.pop(item_id)
