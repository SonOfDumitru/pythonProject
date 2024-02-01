'''
observer este un sablon comportamental care te lasa sa definesti un mecanism tip subscriere
pt a notifica mai multe obiecte despre un eveniment care i se intampla obierctului la care au subscris
Avantaje:
- poti stabili relatii intre obiecte in momentul rularii programului
Dezavantaj:
- subscriberii sunt notificati in ordine aleatoare
'''


from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, observable):
        pass


class Observable(ABC):
    @abstractmethod
    def register_observer(self, observer):
        pass

    @abstractmethod
    def notify(self):
        pass

class Subject(Observable):
    def __init__(self, message):
        self.__message = message
        self.observers = []

    def register_observer(self, observer):
        self.observers.append(observer)

    def notify(self):
        for o in self.observers:
            o.update(self)

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, msg):
        self.__message = msg
        self.notify()


class RealObserverA(Observer):
    def update(self, observable):
        if observable.message.startswith('A'):
            print(f'{self.__class__.__name__} a fost notificat')


class RealObserverB(Observer):
    def update(self, observable):
        if observable.message.startswith('B'):
            print(f'{self.__class__.__name__} a fost notificat')

a = RealObserverA()
b = RealObserverB()
s = Subject('Salut')
s.register_observer(a)
s.register_observer(b)
s.message = 'Ana are mere'
s.message = 'Biblioteca'
