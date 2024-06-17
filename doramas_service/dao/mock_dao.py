from doramas_service.dao.abstract_dao import AbstractDAO


class MockDAO(AbstractDAO):
    def __init__(self):
        self._data = {}

    def add(self, item):
        self._data.update({len(self._data)+1: item})

    def all(self):
        return self._data

    def get(self, reference):
        return self._data[reference]

    def update(self, item_id, item):
        self._data[item_id] = item

    def delete(self, item_id):
        self._data.pop(item_id)
