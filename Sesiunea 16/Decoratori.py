import functools


def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        print('Inainte ca dunctia sa fie apelata')
        func()
        print('dupa ce functia a fost apelata')
    return wrapper

def say_hi():
    print('Hi')

say_hi=my_decorator(say_hi)
say_hi()
print(say_hi)

@my_decorator
def say_hello():
    print('Hello')

say_hello()
print(say_hello)

# sa se scrie un decorator care repeta executia unei functii de 2 ori

def do_twice(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        func(*args,**kwargs)
        return func(*args,**kwargs)
    return wrapper
@do_twice
def return_greeting(name):
    print('Create greating')
    return f'Hi {name}'

r= return_greeting('Bob')
print(r)


# sa se scrie un decorator care executa o functie de n opri , n fiind parametru al decoratorului
def repeat(n):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            for i in range(n):
                func(*args,**kwargs)
        return wrapper
    return decorator_repeat

@repeat(5)
def say_hello():
    print('Hello')

say_hello()
print(say_hello)


def say_hello2():
    print('Hello')
d =  repeat(5)                         #acelasi cu
say_hello2 = d(say_hello2)             #
say_hello2()                           #


repeat(5)(say_hello2())               #asta
()                                    #
                                       


# sa se scrie un decaorator care intarzie apelul unei functii cu o secunda

from time import sleep
def delay(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        sleep(1)
        return func(*args,**kwargs)
    return wrapper

@delay
def scrie():
    print('Hello Kitty!')


scrie()

