def my_function():
    print('Hello din functie')


my_function()


def plus(*args):  # *args este o conventie in py dar se poate numi oricum atat timp cat are "*"
    print(args)
    return sum(args)


plus(1, 2, 3, 4, 5)

plus(1)

plus(*[1, 2, 3])


# 1.Sa se scrie o functie care citeste de la tastatura un text si returneaza toate caracterele folosite in acel string
# ordonate alfabetic.

'''
#    VARIANTA A
def ordon_alfa(sentence):
    litere = [char for char in sentence if char.isalpha()] #new_list = [expression for item in iterable if condition]


    sort_litere = sorted(litere)

    enumerate_litere = list(enumerate(sort_litere, 1))
    return enumerate_litere

sentence = input('Introduce text: ')
enumerated_letters = ordon_alfa(sentence)

for position, letter in enumerated_letters:
    print(f'Letter {position}: {letter}')
'''
'''
#    VARIANTA B
def ordon(sentence):
    litere = [char for char in sentence if char.isalpha]
    sort_l = sorted(litere)
    enumerate_l = list(enumerate(litere,2))
    return enumerate_l

sentence = ('Sorin e la mare distanta de afara')
enumerated_l = ordon(sentence)

print(f'{enumerated_l}')
'''

# 2. Sa se scrie o functie care primeste ca parametri 2 numere si il returneaza pe cel mai mare
'''
def mai_mare(a,b):
    a= numere_a
    b= numere_b
    if a > b:
        print(a)
    else:
        print(b)
numere_a = input('introdu a: ')
numere_b = input('introdu b: ')
mai_mare(numere_a,numere_b)
'''
#3. Scrieţi o funcţie care primeşte ca parametru lungimea laturii unui pătrat şi returnează aria sa.
'''
import math

def aria_patrat(latura):
    return latura*latura

latura = int(input(f'lautra este: '))
aria = aria_patrat(latura)
print(f'aria este: {aria}')
'''

#4. Scrieţi un subprogram care primeşte ca parametru lungimea laturii unui pătrat şi returnează atât
# lungimea diagonalei, cât şi perimetrul pătratului
import math

def patrat(latura):
    diagonal = math.sqrt(2)*latura
    perimetrul = latura * 4
    return perimetrul, diagonal

latura = int(input('lautra este: '))
perimetrul, diagonal = patrat(latura)
print(f'diagonala pentru un patrat cu latura {latura} este: {diagonal}')
print(f'Perimetrul unui patrat cu latura {latura} este {perimetrul}')

# 5. Scrieţi o funcţie care primeşte ca parametri de intrare lungimile celor două catete ale unui triunghi
# dreptunghic şi returnează lungimea ipotenuzei.

def ipotenuza(cateta1,cateta2):
    lipotenuza = (cateta1 * cateta1 + cateta2 * cateta2) ** 0.5
    return lipotenuza

cateta1 = float(input('cateta1 este: '))
cateta2 = float(input('cateta2 este: '))
lipotenuza = ipotenuza(cateta1,cateta2)
print(f'ipotenuza este:{lipotenuza}')

# 5.Scrieţi o funcţie care primeşte 3 parametri de tip real, cu semnificaţia de lungimi pentru 3 segmente.
# Funcţia va returna 1 dacă cele trei segmente pot forma un triunghi şi 0, în caz contrar.

def triunghi(x,y,z):
    if x+y>z and z+y>x and x+z>y:
        return 1
    else:
        return 0
x = int(input('introdu latura x: '))
y = int(input('introdu latura y: '))
z = int(input('introdu latura xz: '))
result = triunghi(x,y,z)

if result:
    print('1')
else:
    print('0')

