# 6. Să se tipărească toate numerele prime aflate între doi întregi citiţi. Programul va folosi o funcţie care testează
# dacă un număr este prim sau nu.
# import math
#
#
# def is_prime(nr):
#     if nr < 2:
#         return False
#     for i in range(2, int(math.sqrt(
#             nr)) + 1):  # optimizare 2: reducerea spatiului de cautare si mai mult, pana la radical din nr
#         #   for i in range(2, nr//2+1):  #optimizare 1: reducerea spatiului de cautarea a numerelor pana la jumatatea lui nr+!
#         if nr % i == 0:
#             return False
#     return True
#
#
# def print_primes_between(start, end):
#     for n in range(start, end + 1):
#         if is_prime(n):
#             print(n)
#
#
# print_primes_between(4, 50)


# 7. Scrieţi un program care tipăreşte numerele întregi găsite între două valori citite, numere care se divid cu suma
# cifrelor lor. Programul va utiliza o funcţie care returnează suma cifrelor unui număr întreg primit ca parametru.

def sum_digits(nr):
    s = 0
    while nr != 0:
        ultima_cifra = nr % 10
        # print(f'ultima_cifra:{ultima_cifra}')
        s += ultima_cifra
        # print(f's:{s}')
        nr = nr // 10
        # print(f'nr:{nr}')
    return s


sum_digits(1234)


def print_numbers_diviz_by_digit_sum(start, end):
    for n in range(start, end + 1):
        if n % sum_digits(n) == 0:
            print(n)


print_numbers_diviz_by_digit_sum(1, 20)

'''
1.Clasa Cerc
    Atribute: rază, culoare
    Constructor pentru ambele atribute
    Metode:
descrie_cerc() - va PRINTA culoarea și raza
aria() - va RETURNA aria 
diametru() 
circumferinta()

2. Clasa Dreptunghi
     Atribute: lungime, lățime, culoare
     Constructor pentru toate atributele
     Metode:
descrie()
aria()
perimetrul()
schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic. Ea va lua ca și parametru o nouă culoare și va 
suprascrie atributul self.culoare. Poți verifica schimbarea culorii prin apelarea metodei descrie().


'''
import math

class Dreptunghi:
    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descrie(self):
        print(f'Dreptunghiul are culoare {self.culoare}, lungimea {self.lungime} si latimea {self.latime}')


    def aria(self):
        return self.latime * self.lungime


    def perimetru(self):
        return 2 * (self.lungime + self.latime)


    def culoare_noua(self, noua_culoare):
        self.culoare = noua_culoare

drept = Dreptunghi(latime=5, lungime=10, culoare="albastru")

drept.descrie()
print(f"Aria dreptunghiului: {drept.aria()}")
print(f"Perimetrul dreptunghiului: {drept.perimetru()}")
drept.culoare_noua('verde')
print(f"Noua culoare este: {drept.culoare}")



class Cerc:
    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare


    def descrie_cerc(self):
        print(f'Cercul are culoare {self.culoare} si raza {self.raza}')


    def aria(self):
        return math.pi * self.raza ** 2


    def diametru(self):
        return 2 * self.raza


    def circumferinta(self):
        return 2 * math.pi * self.raza


cerc1 = Cerc(raza=5, culoare="albastru")

cerc1.descrie_cerc()  # Va afișa: Cercul are culoarea albastru și raza 5.
print(f"Aria cercului: {cerc1.aria()}")  # Va afișa: Aria cercului: 78.53981633974483
print(f"Diametrul cercului: {cerc1.diametru()}")  # Va afișa: Diametrul cercului: 10
print(f"Circumferința cercului: {cerc1.circumferinta()}")
