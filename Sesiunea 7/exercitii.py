'''
Folosește un for că să iterezi prin toată lista și să afișezi;
‘Mașina mea preferată este x’.
Fă același lucru cu un for each.
Fă același lucru cu un while.

'''

# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
#
# for index in range(len(masini)):
#     print(f'Masina mea preferata este {masini[index]}')
#
# for masina in masini:
#     print(f'Masina mea preferata este {masina}')
#
# index = 0
# while index < len(masini):
#     print(f'Masina mea preferata este {masini[index]}')
#     index += 1

'''
2. Aceeași listă:
Folosește un for else
În for
Modifică elementele din listă astfel încât să fie scrise cu majuscule, exceptând primul și ultimul.
În else:
  Printează lista.
  
'''

# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# for index, elem in enumerate(masini):
#     print(index, elem)
#     if index == 0 or index == len(masini) - 1:  # if index in (0,len(masini)-1)
#         masini[index] = elem.lower()
#     else:
#         masini[index] = elem.upper()
# else:
#     print(masini)
#
# for index, elem in enumerate(masini):
#     masini[index] = elem.lower() if index in (0, len(masini) - 1) else elem.upper()
# else:
#     print(masini)

'''
3. Aceeași listă:
Vine un cumpărător care dorește să cumpere un Mercedes.
Iterează prin ea prin modalitatea aleasă de tine.
Dacă mașina e mercedes:
   Printează ‘am găsit mașina dorită de dvs’
   Ieși din ciclu folosind un cuvânt cheie care face acest lucru
Altfel:
   Printează ‘Am găsit mașina X. Mai căutam‘
'''

# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# for masina in masini:
#     if masina == 'Mercedes':
#         print('Am gasit masina dorita de dumneavoastra')
#         break
#     else:
#         print(f'Am gasit masina {masina}. Mai cautam')

'''
4. Aceeași listă;
Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu excepția Trabant și Lăstun. 

Dacă mașina e Trabant sau Lăstun:
   Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie else).
Printează S-ar putea să vă placă mașina x.

'''

# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# for masina in masini:
#     if masina in ('Trabant','Lăstun'):
#         continue
#     print(f'S-ar putea sa va placa masina {masina}')


'''
5. Modernizează parcul de mașini:

Crează o listă goală, masini_vechi.
Iterează prin mașini.
Când găsesti Lăstun sau Trabant:
Salvează aceste mașini în masini_vechi.
Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
Printează Modele vechi: x.
Modele noi: x.

'''
#
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# masini_vechi = []
#
# for index, masina in enumerate(masini):
#     if masina in ('Trabant', 'Lăstun'):
#         masini_vechi.append(masina)
#         masini[index] = 'Tesla'
# print(f'Modele vechi:{masini_vechi}')
# print(f'Modele noi {masini}')

'''
6. Având dict:
pret_masini = {
    'Dacia': 6800,
    'Lăstun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}

Vine un client cu un buget de 15000 euro.

Prezintă doar mașinile care se încadrează în acest buget.
Iterează prin dict.items() și accesează mașina și prețul.
Printează Pentru un buget de sub 15000 euro puteți alege mașină xLastun
Iterează prin listă.

'''
# pret_masini = {
#     'Dacia': 6800,
#     'Lăstun': 500,
#     'Opel': 1100,
#     'Audi': 19000,
#     'BMW': 23000
# }
# for masina,pret in pret_masini.items():
#     if pret<15000:
#         print(f'Pentru un buget de sub 15000 euro puteți alege mașină {masina}')

'''
12. Aceeași listă:
Ordonează crescător lista fară să folosești sort.
Te poți inspira vizual de aici.
https://www.youtube.com/watch?v=lyZQPjUT5B4

'''

# numere = [5,7,3,9,3,3,1,0,-4,3]
#
# for i in range(0,len(numere)-1):
#
#     for j in range (i+1,len(numere)):
#         if numere[j]<numere[i]:
#             numere[i],numere[j] = numere[j],numere[i]
# print(numere)

'''

11.
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
Itereaza prin listă alte_numere 
Populează corect celelalte liste
Afișează cele 4 liste la final

'''

alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []

for x in alte_numere:
    if x % 2 == 0:
        numere_pare.append(x)
    else:
        numere_impare.append(x)
    if x > 0:
        numere_pozitive.append(x)
    else:
        numere_negative.append(x)
print(numere_pare)
print(numere_impare)
print(numere_negative)
print(numere_pozitive)

'''
7. Având lista:
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
Iterează prin ea.
Afișează de câte ori apare 3 (nu ai voie să folosești count).

'''

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
counter = 0

for n in numere:
    if n == 3:
        counter += 1
print(counter)

'''
8. Aceeași listă:
Iterează prin ea
Calculează și afișează suma numerelor (nu ai voie să folosești sum).

'''
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
s = 0

for n in numere:
    s += n
print(s)

'''
9. Aceeași listă:
Iterează prin ea.
Afișază cel mai mare număr (nu ai voie să folosești max).
'''
max = numere[0]
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
for n in numere[1:]:
    if n > max:
        max = n
print(f'numarul max este {max}')

'''

10. Aceeași listă:
Iterează prin ea.
Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
Ex: dacă e 3, să devină -3
Afișază noua listă.

'''
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
#
# for index, n in enumerate(numere):
#     if n > 0:
#         numere[index] = -n
# print(numere)

'''
13. Sa se scrie un program care citeste de la tastatura litere pana se introduce un caracter care nu este litera. 
La final va afisa toate literele unice si sortate.
'''

# litere = set()
# l = input('introdu litera: ')
# while l.isalpha():
#     litere.add(l)
#     l = input('introdu litera: ')
# print(litere)
# # litere= list(litere)
# # litere.sort()
# # print(litere)


'''
14.Sa se scrie un program care citeste de la tastatura o lista de fructe, iar la final le va afisa doar pe cele care 
incep cu litera a.

15.Fie dictionarul {”a”: 6, “b”: 9}. Fiecare element din dictionar sa se afiseze sub formatul cheie → valoare pe cate
un rand nou.

16.Sa se scrie un program care citeste de la tastatura 6 numere, si apoi le afiseaza pe cele mai mari decat 9.

17.Sa se scrie un program care citeste de la tastatura o lista si apoi un numar si sa se afiseze de cate ori apare in 
lista acel numar.
'''

# fructe = list()
# f = input('introdu fruct: ')
#
# while f.isalpha():
#     if f.startswith('a'):
#         fructe.append(f)
#     f = input('introdu fruct: ')
# print(fructe)


# dic = {'a': 6, 'b': 9}
# for keys,value in dic.items():
#     print(keys, value)

# limit = 6
# lista = []
#
# for i in range(limit):
#     num = int(input(f'introdu numar {i + 1}:'))
#     lista.append(num)
#     lista.sort()
#     lista.reverse()
# print(lista)

limita = 6
lista1 = []

for i in range(limita):
    numere = int(input(f'introdu numar {i + 1}:'))
    lista1.append(numere)
numar = int(input('introdu singularitatea: '))
print(lista1.count(numar))
