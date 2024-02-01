class Animal:
    def __init__(self, age, specie):
        self.age = age
        self.specie = specie

    def eat(self):
        return f'eu sunt un {self.__class__.__name__}:{self.specie} mancacios'

class DomesticaAnimal(Animal):
    def __init__(self, age, specie, propietar):
        super().__init__(age, specie)
        self.propietar = propietar


class WildAnimal(Animal):
    def __init__(self, age, specie, location):
        super().__init__(age, specie)
        self.location = location


def animals_eat(animals):
    for a in animals:
        print(a.eat())

animals_eat([
    DomesticaAnimal(5,'vaca','ion'),
    DomesticaAnimal(4,'caine','ion'),
    WildAnimal(10,'urs','padure'),
    WildAnimal(40,'girafa','savana')

])

'''
polimorfismul se refera la abilitatea unui obiect de a se comporta in mai multe moduri, in functie de context.
in esenta polimorfismul permite obiectelor de acelasi tip sa aiba comportamente diferite, fara a fi necesar sa se 
stie tipul lor inainte de executie
'''
