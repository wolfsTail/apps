from abc import ABC, abstractmethod


class AbstractDAO(ABC):
    @abstractmethod
    async def add(self, item):
        raise NotImplementedError
    
    @abstractmethod
    async def all(self):
        raise NotImplementedError

    @abstractmethod
    async def get(self, item_id):
        raise NotImplementedError
    
    @abstractmethod
    async def update(self, item_id, item):
        raise NotImplementedError

    @abstractmethod
    async def delete(self, item_id):
        raise NotImplementedError
