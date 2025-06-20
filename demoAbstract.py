
from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def hello(self):
        pass

class Cat(Animal):
    def hello(self):
        print("hello from cat")

cat = Cat()
print(cat.hello())

# animal = Animal()