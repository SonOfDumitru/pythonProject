class Dog:
    species = 'mamifer'  # acest tip de atribut este unul special --> class attribute (are aceiasi valoare pentru toate
                         # obiectele din aceasta clasa)
    age = 8
    name = "Bruno"


d = Dog()  # instantierea unui obiect (d -> obiect)

print(d.name)

d2 = Dog()
d2.name = "Puffy"  # name devine atribut de instanta pentru obiectul d2
print(d.name, d2.name)

Dog.name = 'RExy'   #name modifica atributul din clasa Dog
print(d.name, d2.name)


# atributele de clasa sunt in general folosite pentru a defini constante intr-o clasa

class Cat:
    species = 'mamifer'

    def __init__(self, age, name):  # functie constructor
    # self este o referinta catre obiectul curent
        self.age = age
        self.name = name

c = Cat(age =1, name ='leu')
c2 = Cat(age =4, name ='mata')
print(c.age,c2.age,c.species,c.name)
# C.name -> incorect deoarece atributul name este un atribut de instanta si poate fi accesat printr-un obiect din aceasta clasa
# (pentru ca este creat in constructor si nu in clasa)

