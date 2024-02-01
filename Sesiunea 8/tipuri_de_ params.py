##################################################################################################################

def plus(a, b):  # a si b sunt parametrii (numele folosite pentru argumentele unei funtii)
    return a + b


plus(1, 2)  # 1 si 2 sunt argumente (argumentele sunt valorile parametrilor)


##################################################################################################################

# default arguments (parametrii cu valori implicite

def plus(a, b=2):
    return a + b


plus(1)  # daca nu specificam o valoare explicita pentru b, atunci va lua valoarea implicita 2
plus(1, 3)


##################################################################################################################

# keyword arguments

def plus(a, b):
    return a + b


plus(a=1, b=2)
plus(b=2, a=1)  # specificand argumentele prin numele lor nu mai este necesar sa pastram ordinea


##################################################################################################################

# numar variabil de parametrii

def plus(*args):  # *args este o conventie in py dar se poate numi oricum atat timp cat are "*"
    print(args)
    return sum(args)


plus(1, 2, 3)
plus(1)
plus(*[1, 2, 3])  # * = unpacking


def plus(**kwargs):
    print(kwargs)
    return sum(kwargs.values())


plus(a=1, b=2)
plus(**{'a': 1, 'b': 2})


def plus(*args, **kwargs):
    print(args, kwargs)
    return sum(args) + sum(kwargs.values())


plus(1, 2, a=7, x=9)
plus(3)
plus(x=7, y=8)
plus()
