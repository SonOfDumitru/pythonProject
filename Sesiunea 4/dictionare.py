#creare
print(20 * '_', 'creare', 20 * '_')


car ={
    'brand':'ford',
    'model':'mustang',
    'an': '1929'
}

#accesare elemente
print(20 * '_', 'accesare elemente', 20 * '_')

print(car['brand'])  #crapa daca nu gaseste elementu
print(car.get('model'))
print(car.get('is_new'))
print(car.get('is_new',True))

#adaugare elemente
print(20 * '_', 'adaugare elemente', 20 * '_')

car['is_new']=True
print(car)

car.setdefault('is_old',True) #returneaza valoarea de la cheia data si daca aceasta nu exista o adauga cu valoarea din paranteza
print(car)
car.setdefault('price',7910)
print(car)

#stergere elemente
print(20 * '_', 'stergere elemente', 20 * '_')

car.pop('is_new')
print(car)

car.popitem() #elimina ultima cheie inserata
print(car)

del car['an']
print(car)

#stergere toate elemente
print(20 * '_', 'stergere toate elementele', 20 * '_')

car.clear()
print(car)

#afisare toate chei
print(20 * '_', 'afisare toate chei', 20 * '_')

car ={
    'brand':'ford',
    'model':'mustang',
    'an': 1929
}

print(list(car.keys()))

#afisare toate valorile
print(20 * '_', 'afisare toate valorile', 20 * '_')

print(list(car.values()))

#afisare toate valorile +elemente
print(20 * '_', 'afisare toate valorile = elemente', 20 * '_')

print(list(car.items()))
