from abc import ABC, abstractmethod

class DBEntity(ABC):
    @abstractmethod
    def save_to_db(self):
        pass
    
    @abstractmethod
    def update(self):
        pass
    
    @abstractmethod
    def delete(self):
        pass

    @abstractmethod
    def display_info(self):
        pass