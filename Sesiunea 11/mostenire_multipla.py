class Car:
    def go(self):
        print('vrumvrum')

    def start(self):
        print('starting car')


class Flyable:
    def fly(self):
        print('fly fly')

    def start(self):
        print('starting flyable')


class FlyingCar(Car, Flyable):
    pass


c = FlyingCar()

c.go()
c.fly()
c.start()

# MRO - Method resolution order: - se decide care functie din clasa car sau flyable se va apela de la stanga la dreapta
