'''
listele sunt folosite pentru a stoca mai multe valori intr-o singura variabila
elementele dintr-o lista sunt ordonabile, modificabile si permit valori duplicate
listele sunt indexate si primul element are indexul 0
cand spunem ca o lista este ordonata ne referim la faptul ca elementele au o ordine predefinita si
acea ordine nu se va schimba
'''

# creare

fructe = ['mere', 'pere', 'banane','cocos','afine']
numere = [1, 2, 3, 4, 5, 6]
masini = list(('audi', 'tesla', 'dacia'))


print(type(numere))
print(len(numere))

# indexare
print(20 * '_', 'indexare', 20 * '_')

print(numere[0])
print(fructe[1])
print(numere[-1])
print(numere[:2])  # sa afiseze pana la indexul 2 din lista, mai putin 2
print(fructe[:4])
print(numere[::2])  # sa mearga din 2 in 2
print(numere[:])  # de la inceput pana la final
print(numere[::-1]) # printeaza de la cap la coada

# adaugare element
print(20 * '_', 'adaugare element', 20 * '_')

numere.append(10)
print(numere) # adauga elementul 10 in lista

numere.insert(2,9) #la indexul 2 s-a adaugat elementul 9
print(numere)

# stergere
print(20 * '_', 'stergere element', 20 * '_')


elem=numere.pop() #elimina de la final
print(elem) #retunreaza ultimul element eliminat
print(numere) #returneaza lista fara ultimul element

numere.pop(0) #elimina de la indexul specificat
print (numere)

numere.remove(3) #sterge elementul specificat dupa valoare
print(numere)

# sterge toate elementele
print(20 * '_', 'stergere toate elementele', 20 * '_')

numere.clear() #sterge toate elementele
print(numere)

# inlocuire element
print(20 * '_', 'inlocuire element', 20 * '_')

print(fructe)
fructe[1]='struguri'
print(fructe)

#numarare aparitii
print(20 * '_', 'numarare aparitii', 20 * '_')

numere = [1, 2, 3, 4, 5 ]
print(numere.count(2))

#adunare a 2 liste
print(20 * '_', 'adunare a 2 liste', 20 * '_')

numere2 = [20,21,22]
numere.extend(numere2)
print(numere)
numere3 = [1,2,3]
print(numere2 +numere3)

#inversare
print(20 * '_', 'inversare', 20 * '_')

print(fructe[::-1]) #nu modifica lista initiala ci incepe de la indexul -1
print(fructe[1:2:1])
fructe.reverse() #modifica lista initiala(operatiune in place)
print(fructe)


#sortare


numere.sort()
print(numere)
numere.sort(reverse=True)
print(numere)
