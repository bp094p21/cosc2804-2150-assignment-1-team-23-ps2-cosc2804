from abc import ABC, abstractmethod


# abstract base class for all types of buildings. allows for polymorphic use within framework inner workings.
# all types of buildings should inherit from this class and provide implementation for the corresponding build() method.
class Building(ABC):

    @abstractmethod
    def build(self):
        pass
