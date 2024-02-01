'''
Implementati un iterator numit ReverseIterator, care parcurge o colectie in sens opus. Exemplu de folosire:

note = [3, 7, 5, 8, 10]
rev_it = ReverseIterator(note)
print(next(rev_it))  # printeaza 10
print(next(rev_it))  # printeaza 8
print(next(rev_it))  # printeaza 5
s.a.m.d
'''
import functools
from datetime import datetime
from random import randint
from time import perf_counter, sleep


class ReverseIterator():
    def __init__(self,collection):
        self.collection =  collection
        self.start = len(collection)-1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start<0:
            raise StopIteration
        curent_index =  self.start
        self.start -= 1
        return self.collection[curent_index]

note = [3, 7, 5, 8, 10]
rev_it = ReverseIterator(note)
print(next(rev_it))  # printeaza 10
print(next(rev_it))  # printeaza 8
print(next(rev_it))  # printeaza 5
rev_it = ReverseIterator(note)
for elem in rev_it:
    print(elem)

print( 50 * '-')
'''
Implementați un generator pentru loteria 6/49 și noroc:
Primele 6 apelări către generator vor da cate un numar intre 1 si 49 (inclusiv)
Ultima apelare va da un singur număr de “noroc” format din 7 cifre

'''

# def loterie_gen():
#     for i in range(6):
#         yield randint(1, 49)
#     yield randint(1_000_000,9)
#
# for i in loterie_gen():
#     print(i)
#
#
#
# def loterie_gen_unice():
#     generate = set()
#     for i in range(6):
#         nr  = randint(1, 49)
#         while nr in generate:     # cat timp numarul generat a mai fost generat inca o data pana acum, genereaza un nou numar
#             nr  = randint(1, 49)
#             generate.add(nr)    # adauga numarul nou in setul de numere generate pana acum
#         yield nr
#
#     yield randint(1_000_000,9)
#
# for i in loterie_gen():
#     print(i)
#
# print( 50 * '-')

'''
Implementați următorii decoratori:
timeit – decorator care măsoară timpul de execuție al unei funcții 
logger – decorator care printeaza argumentele de intrare, și rezultatul unei funcții

'''

def timeit(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        start = perf_counter()
        result = func(*args,**kwargs)
        print(f'A durat {perf_counter() -  start} secunde')
        return result
    return wrapper

@timeit
def say_hello():
    sleep(3)
    print('functie executata')

say_hello()


def logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'Rezultat: {result}')
        print(f'Argumente pozitionale {args}')
        print(f'Argumente cu nume {kwargs}')
    return wrapper
@logger
def name(first,last):
    return f'{first}-{last}'

name('Adrian',  last='Andrei')


'''
Decorators extra
Implementați o clasă User, cu următoarele cerințe:
– constructorul va primi nume, email, parola, și data nasterii 
– o metoda login, care va primi email și parola ca parametrii; dacă acestea sunt corecte, userul va fi marcat ca logat
– o metoda get_info, care va returna toate informațiile despre user DOAR DACĂ acesta este logat, folosind un decorator `@require_login` 
– o metoda logout, fara params, care delogheaza userul.


Se va testa apelarea metodei get_info inainte de logare, dupa logare, dupa delogare, și după încă o logare.

'''
def require_logged_in(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        if self.is_logged_in:
            return func(self, *args, **kwargs)

    return wrapper


class User:
    def __init__(self, nume, email, parola, data_nasterii):
        self.nume = nume
        self.email = email
        self.parola = parola
        self.data_nasterii = data_nasterii
        self.__logat = False

    def login(self, email, parola):
        if email == self.email and parola == self.parola:
            self.__logat = True
    @require_logged_in
    def get_info(self):
        return f'Nume: {self.nume}, Email: {self.email}, Data Nasterii: {self.data_nasterii}, Parola: {"*" * len(self.parola)}'

    def logout(self):
        self.__logat ==False

    @property
    def is_logged_in(self):
        return self.__logat

u = User('Adrian Andrei', 'adrianandrei@gmail.com', 'parola123', '01.01.90')
print(u.get_info())
u.login('adrianandrei@gmail.com', 'parola123')
print(u.get_info())
u.logout()
print(u.get_info())

print(60 * '~')
'''
6. Sa se scrie un decorator care primeste ca parametru doua ore, 
reprezentand datele limita intre care sa se execute functiile decorate.
'''

def only_execute_between(start, end):
    def decorator_execute_between(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if start <= datetime.now().hour <= end:
                return func(*args, **kwargs)

        return wrapper

    return decorator_execute_between


@only_execute_between(18,20)
def hello():
    print('Hello World!')

hello()
