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
        updating_item = self._data[item_id]
        for key in item.keys():
            if key in updating_item:
                updating_item[key] = item[key]
        return self._data[item_id]

    async def delete(self, item_id):
        self._data.pop(item_id)
