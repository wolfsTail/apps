from abc import ABC, abstractmethod


class AbstractDAO(ABC):
    @abstractmethod
    def add(self, item):
        raise NotImplementedError
    
    @abstractmethod
    def all(self):
        raise NotImplementedError

    @abstractmethod
    def get(self, reference):
        raise NotImplementedError
    
    @abstractmethod
    def update(self, item_id, item):
        raise NotImplementedError

    @abstractmethod
    def delete(self, reference):
        raise NotImplementedError
