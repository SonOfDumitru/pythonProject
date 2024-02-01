from abc import abstractmethod, ABC
from dataclasses import dataclass


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

@dataclass
class Person(Observer):
    nume: str

    def update(self, observable):
        last_message = observable.get_last_message()
        if last_message.content.startswith(self.nume):
            print(f'{self.nume} am primit un mesaj')

    def send_message(self, chat_room):
        message = input(f'{self.nume} Introdu un mesaj: ')
        chat_room.add_message(Message(self, message))

@dataclass
class Message:
    author: Person
    content: str


class ChatRoom(Observable):
    def register_observer(self, observer):
        self.observers.append(observer)
    def get_last_message(self):
        return self.messages[-1]

    def notify(self):
        for o in self.observers:
            o.update(self)

    def __init__(self):
        self.messages = []
        self.observers = []

    def add_message(self, message):
        self.messages.append(message)
        self.notify()

c = ChatRoom()
t = Person('Tim')
p = Person('Peter')
a = Person('Ana')

c.register_observer(a)
c.register_observer(p)
c.register_observer(t)

t.send_message(c)
