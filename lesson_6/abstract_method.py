from abc import ABC, abstractmethod

class Base(ABC):

    @abstractmethod
    def my_method1(self):
        ...

    @abstractmethod
    def my_method2(self):
        ...

class Child(Base):

    def my_method1(self):
        print(1)

    def my_method2(self):
        print(2)

a = Child()