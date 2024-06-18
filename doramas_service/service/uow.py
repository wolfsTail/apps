from abc import ABC, abstractmethod

from doramas_service.dao import MockDAO


class AbstractUnitOfWork(ABC):
    doramas: MockDAO

    @abstractmethod
    def __init__(self):
        raise NotImplementedError

    @abstractmethod
    async def __aenter__(self):
        raise NotImplementedError

    @abstractmethod
    async def __aexit__(self, *args):
        raise NotImplementedError

    @abstractmethod
    async def commit(self):
        raise NotImplementedError

    @abstractmethod
    async def rollback(self):
        raise NotImplementedError


class MockUnitOfWork(AbstractUnitOfWork):
    def __init__(self, data=None):
        if data is None:
            data = {}
        self.doramas = MockDAO(data)
        self.committed = False

    async def __aenter__(self):
        return self

    async def __aexit__(self, *args):
        pass

    async def commit(self):
        self.committed = True

    async def rollback(self):
        pass
