'''
7. Citește de la tastatură:
lungimea;
lățimea.
   Afișează: 'Aria dreptunghiului este x'.
   Formula ariei: l*l
   '''

L=int(input('Lungime:'))
l=int(input('latime:'))

print (f'Aria dreptunghiului este {l*L}')  #f din fata permite scriereade cod in string



'''
8.8. Având stringul: 'Coral is either the stupidest animal or the smartest rock':
afișează de câte ori apare cuvântul 'the';
'''
'''
string='Coral is either the stupidest animal or the smartest rock'
print(string.count(' the ')) #de cate ori apare cuvantul the in string
'''

'''
9. Același string:
Inlocuieste 'the' cu 'THE' peste tot;
Printează rezultatul.
'''
'''
print(string.replace(' the ',' THE '))
'''

'''
10. Același string:
Folosește un assert ca să verifici dacă acest string conține doar numere.
'''
'''
string='Coral is either the stupidest animal or the smartest rock'
assert string.isdigit() #daca e corect nu returneaza nimic, daca e incorect da eroare
'''

'''
11. Exercițiu:
citește de la tastatură un string de dimensiune impară;
afișează caracterul din mijloc.
'''
'''
string=input ('Inotrodu un string: ')
# 0 1 2 3 4 -exemple
# a b c d e -exemple

index_mijloc = len(string) // 2
print(string[index_mijloc])
'''

'''
12. 
citește un string de la tastatură (ex: 'alabala portocala');
salvează fiecare cuvânt într-o variabilă;
printează ambele variabile pentru verificare.
'''
'''
string=input ('iNTRODU UN STRING: ')
s1,s2=string.split()
print(s1)
print(s2)
'''

'''
13. Exercițiu:
citește un string de la tastatură (ex: alabala portocala);
salvează primul caracter într-o variabilă - indiferent care este el, încearcă cu 2 stringuri diferite;
capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul caracter => alAbAlA portocAla.
'''
'''
string=input ('iNTRODU UN STRING: ')

first = string[0] #cand avem index punem paranteze []
interior_modificat = string[1:-1].replace(first, first.upper())
final_string = string[0] + interior_modificat + string[-1]
print(final_string)
'''

'''
14.Exercițiu:
citește un user de la tastatură;
citește o parolă;
afișează: 'Parola pt user x este ***** și are x caractere';
***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie să afișeze corect.

eg: parola abc => ***
      parola abcd => ****
'''

user = input('introdu username: ')
parola = input('introdu parola: ')

stelute = '*' * len(parola)
print(f'parola pt user {user} este {stelute} si are {len(parola)} caractere')
