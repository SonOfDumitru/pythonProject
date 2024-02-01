'''
o clasa abstracta care are cel putin o metoda abstracta
o metoda abstracta este o metoda fara implementare(fara corp)
'''

from abc import ABC, abstractmethod  # (abstract base class)


class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def sleep(self):
        raise NotImplementedError


class Dog(Animal):
    def sound(self):
        print('buff')

    def sleep(self):
        print('zzzz')

c=Dog()
print(c)
