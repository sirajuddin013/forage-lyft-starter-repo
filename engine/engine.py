  from abc import ABC, abstract-method

 class Engine(ABC):
    @abstractmethod
    def needs_service(self):
        pass