from abc import abstractmethod, ABCMeta
from abc import ABC


class Animal(ABC):


    @abstractmethod
    def sound():

        pass


class Dog(Animal):

    def sound(self):

        print("bark bark")


class Tiger(Animal):

    def sound(self):

        print("cry cry...")



d = Dog()
T = Tiger()

d.sound()
T.sound()