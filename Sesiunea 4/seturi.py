# seturile sunt colectii de elemente unice si neordonabile

#creare
print(20 * '_', 'creare', 20 * '_')

fructe = {'mar','par','banana'}

masini = set()  # asa se creaza un set fara elemente

#adaugare elemente
print(20 * '_', 'adaugare elemente', 20 * '_')

fructe.add('struguri')   # nu are o ordine unde se adauga elementul
print(fructe)

#stergere elemente
print(20 * '_', 'stergere elemente', 20 * '_')

fructe.remove('banana')
print(fructe)

#fructe.remove('cirese') - Arunca EROARE pt ca cirese nu exista
print(fructe)
fructe.discard('cirese') # Nu arunca eroare
fructe.pop()
print(fructe)
fructe.clear()
print(fructe)


#Operatiuni speciale
# 1.Join
print(20 * '_', 'Join', 20 * '_')

set1={1,2,3}
set2={'a','b','c'}

set3=set1.union(set2)
print(set3)

print(set1 | set2)

# 2. Intersectia = afiseaza elementele comune
print(20 * '_', 'Intersectia', 20 * '_')

x={'apple','banan','cherry'}
y={'google','microsoft','apple'}

z = x.intersection(y)
print(z)
print(x & y)

# 3. Diferenta
print(20 * '_', 'Diferenta', 20 * '_')

x={'apple','banan','cherry'}
y={'google','microsoft','apple'}

z=x.difference(y)
print(z)
print(x-y)
print(y-x)


# 4. Diferenta simetrica
print(20 * '_', 'Diferenta simetrica', 20 * '_')

x={'apple','banan','cherry'}
y={'google','microsoft','apple'}

z=x.symmetric_difference(y) # se printeaza toate elementele care nu sunt comune
print(z)
print(x^y)
print(y^x)

# 4. Subset si superset
print(20 * '_', 'Subset si superset', 20 * '_')

a={1,2,3}
b={5,4,3,2,1}

print(a.issubset(b))    #toate elementele lui a sunt in b
print(b.issuperset(a)) # setul b contine toate elementele din a
print(a.issuperset(b)) # setul a contine toate elementele din b
