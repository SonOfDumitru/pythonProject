from dataclasses import dataclass, field
from typing import List

'''
dataclass suprascrie automat 3 functii:
1. __init__ (constructorul)
2. __repr__ (afisare)
3. __eq__ (egalitatea daca toate campurile sunt egale)
'''
@dataclass

class Student:
    name:str
    age:int

s = Student('Andrei', 20)
print(s)
s2 = Student('Andrei', 20)
print(s==s2)

@dataclass
class Teacher:
    name:str
    materie:str
    vechime: int=0 #specificare valoare implicita
    clase: List =field(default_factory=list) # se creeaza o lista goala pentru fiecare obiect nou
    cod_intern: int= field(init=False,repr=False) #acest atribut nu va fi adaugat in constructor si nici in afisare
t=Teacher('Valeria','matematica')
print(t)
