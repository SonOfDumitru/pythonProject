class Person:
    def __init__(self, name, age):
        self.name = name
        self.age= age

class Vehicle:
    def __init__(self, type, capacity,power,owner):
        self.type = type
        self.capacity =  capacity
        self.power = power
        self.owner = owner

    def ride(self):
        return None

class UtilityVehicle(Vehicle):
    def __init__(self,load_capacity, capacity, power , owner):
        super().__init__('utility_vehicle', capacity, power, owner)
        self.load_capacity = load_capacity

class Car(Vehicle):
    def __init__(self,capacity,power,owner, fuel_type):
         super().__init__('car', capacity, power, owner)
         self.fuel_type = fuel_type

    def ride(self):
        print(f'{self.owner.name} ride a {self.type}')
class Bike(Vehicle):
    def __init__(self,capacity,power,owner):
        super().__init__('bike',capacity,power, owner)

class Bus(Car):
    def __init__(self,capacity,power,owner, fuel_type, passengers_type):
         super().__init__( capacity, power, owner, fuel_type)
         self.passengers_type = passengers_type

class MotorBike(Bike):
    def __init__(self, capacity,power,owner,engine_capacity):
        super().__init__(capacity,power, owner)
        self.engine_capacity = engine_capacity

p1 = Person("Sergiu", 24)
p2 = Person("Valentina", 23)

VEHICLES = [
    Car(capacity=5, power=90, owner=p1, fuel_type="benzina"),
    Car(capacity=5, power=105, owner=p2, fuel_type="benzina"),
    Car(capacity=5, power=60, owner=p1, fuel_type="motorina"),
    Bus(capacity=40, power=150, owner=p2, fuel_type="motorina", passengers_type="elevi"),
    Bus(capacity=35, power=150, owner=p1, fuel_type="motorina", passengers_type="angajati"),
    Bike(capacity=1, power=5, owner=p1),
    MotorBike(capacity=1, power=80, owner=p2, engine_capacity=500),
    MotorBike(capacity=1, power=75, owner=p1, engine_capacity=250),
    UtilityVehicle(capacity=1, power=200, owner=p1, load_capacity=90),
    UtilityVehicle(capacity=1, power=150, owner=p2, load_capacity=100),
]

# Sa se gaseasca toate vehiculele cu capacitate de mai mult de 2 persoane
# Sa se gaseana numele persoanelor care detin o Bike
# Sa se gaseasca toate UtilityVehicle

def find_vehicle_weight_capacity_greater_than_2(vehicles):
    result = []
    for x in vehicles:
        if x.capacity > 2:
            result. append(x)
    return result

print(find_vehicle_weight_capacity_greater_than_2(VEHICLES))

def find_bike_owners(Vehicles):
    result = set()
    for x in VEHICLES:
        if isinstance(x,Bike):
            result.add(x.owner.name)
    return list(result)

print(find_bike_owners(VEHICLES))

def find_all_utility_vehicles(Vehicles):
    result = []
    for x in Vehicles:
        if isinstance(x, UtilityVehicle):
            result.append(x)

    return result
print(find_all_utility_vehicles(VEHICLES))
