
name = 'DRAgos'
print(name)

#lungimea unui string
print(len(name))


#convertire la uppercase
print(name.upper())

#convertire la lowercase
print(name.lower())

#numar de aparitii
nume = 'ana maria'
print(nume.count('a'))
print(nume.count('a')) #ctrl + d face duplicate la linia curenta

print(nume.count('i'))

#prima litera uppercase
print(nume.capitalize())

#inlocuire de text
prop = ' - oare vreau sa merg acolo! \n - unde sa merg?' # \n -> linie noua
print(prop)
print(prop.replace('?','!'))
print(prop) #functia replace nu modifica stringul initial

#index - pozitia ordinara a unui caracter
name = 'john'
print(name.index('o')) #numerotarea incepe de la 0
print(name[0]) # afiseaza caracterul corespunzator indexului
print(name[-1]) # afiseaza caracterul corespunzator indexului dar incepand de la sfarsitul stringului

#slicing
b = 'hello world'
print(b[2:5]) #afiseaza de la 2 la 5, fara 5
print(b[:5])
print(b[2:])
print(b[-8:-2])
