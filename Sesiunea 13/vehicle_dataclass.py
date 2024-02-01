from dataclasses import dataclass, field


@dataclass
class Person:
    name: str
    age: int


@dataclass
class Vehicle:
    type: str
    capacity: int
    power: int
    owner: Person

    def ride(self):
        return (f'{self.owner.name} ride a {self.type}')


@dataclass
class UtilityVehicle(Vehicle):
    type: str = field(init=False, default='utility vehicle')
    load_capacity: int


@dataclass
class Car(Vehicle):
    type: str = field(init=False, default='car')
    fuel_type: str


@dataclass
class Bike(Vehicle):
    type: str = field(init=False, default='bike')


@dataclass
class Bus(Car):
    passenger_type: str


@dataclass
class MotorBike(Bike):
    engine_capacity: int
