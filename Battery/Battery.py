from abc import ABC, abstract_method


  class Battery(ABC):
    @abstract_method
    def needs_service(self):
      pass