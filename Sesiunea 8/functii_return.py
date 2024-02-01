def say_hello():
    return 'hello' #functia se opreste din executie si se va intoarce in locul in care a fost apelata dand inapoi valoare hello

text = say_hello()
print(text)
print(say_hello())


def say_hi():
    print('hi')

text=say_hi()
print(text) #???? dc primesc valaore none
