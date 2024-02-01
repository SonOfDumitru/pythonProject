
#21. Având stringul '0123456789'
#Afișează doar numerele pare
#Afișează doar numerele impare
#(hint: folosește slicing, controlează din pas)

'''
string = '0123456789'
print(string[::2])  # pas vine de la al 2-lea ":" si cate sarim "2" sau "3"
print(string[::3])  # pas vine de la al 2-lea ":" si cate sarim "2" sau "3"
print(string[1::2])
'''


#20.  Citește de la tastatură un string
#Verifică dacă primul și ultimul caracter sunt la fel. Se va folosi un assert
#Atenție: se dorește ca programul să fie case insensitive - 'apA' e acceptat

'''
string = input('introdu ceva text aici: ')
assert string[0].lower() == string[-1].lower()  # daca da eroare nu sunt la fel, daca nu da eroare sunt la fel
'''


#19.Joc ghicit zarul
#Caută pe net și vezi cum se generează un număr random
#Ne imaginăm ca dai cu zarul și salvăm acest număr în dice_roll
#Ia numărul ghicit de la utilizator
#Verifică și afișează dacă utilizatorul a ghicit
#Vei avea 3 opțiuni
#Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y.
#Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y.
#Ai ghicit. Felicitări! Ai ales x si zarul a fost y.

'''
import random
zar= random.randint(1,6)

ghici = int(input('numar zar '))
if ghici<zar:
    print(f'Ai pierdut. Ai ales un numar mai mic. Ai ales {ghici} dar a fost {zar}')
elif ghici> zar:
    print (f'Ai pierdut. Ai ales un numar mai mare. Ai ales {ghici} dar a fost {zar}')
else:
    print(f'Ai ghicit. Felicitări! Ai ales {ghici} si zarul a fost {zar}')
'''

'''
8. X, y, z - laturile unui triunghi.
Afișează dacă triunghiul este isoscel, echilateral sau oarecare.
'''
'''
print(' Introduceti lungimea laturilor unui triunghi: ')
x=int(input('x: '))
y=int(input('y: '))
z=int(input('z: '))

if x==y==z:
    print('echilateral')
elif (x != y != z) :
    print ('oarecare')
else:
    print ('isoscel')
'''


#9. @@@@ @@@@@ @@@@Citește o literă de la tastatură.
#   Verifică și afișează dacă este vocală sau nu.


ch = input('introdu caracter: ')


if(ch=='A' or ch=='a' or ch=='E' or ch =='e' or ch=='I'
 or ch=='i' or ch=='O' or ch=='o' or ch=='U' or ch=='u'):
    print(ch, 'e vocala')
elif ch.isdigit():
    print(ch, 'is a number')
else :
    print(ch, 'consoana')


#10. @@@@ @@@@@ @@@@    Transformă și printează notele din sistem românesc în  >
#Peste 9 => A
#Peste 8 => B
#Peste 7 => C
#Peste 6 => D
#Peste 4 => E
#4 sau sub => F

nota = float(input('introduce o nota: '))
if (9 <= nota <=10 ):
    print(nota,'este calificativul A')
elif (8 < nota <=9 ):
    print(nota,'este calificativul B')
elif (7 < nota <=8 ):
    print(nota,'este calificativul C')
elif (6 < nota <=7 ):
    print(nota,'este calificativul D')
elif (4 < nota <=6 ):
    print(nota,'este calificativul D')
else :
    print(nota,'este calificativul F')



#11.  @@@@@ @@@@@ @@@@@ @@@@@  Verifică dacă x are minim 4 cifre (x e int).
#(ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)

'''

x= str(input('Introdu un numar '))
x1 = int(x)


if  (4 < len(x)) :
    print('valid', len(x))
else:
    print('x')
'''
# 12. @@@ @@@@@@ @@@@@@      Verifică dacă x are exact 6 cifre.

'''
if (5 < len(x) < 7) :
    print('valid', len(x))
else:
    print('x')
'''

#13. @@@@ @@@@@@ @@@@@@   Verifică dacă x este număr par sau impar (x e int).
'''
if x1%2 == 0 :
     print('x e par')
else :
    print('impar')
'''

# 14 @@@@   @@@@@@@@ @@@@@@@  @@@@@@@ 14.  x, y, z (int)
#Afișează care este cel mai mare dintre ele?

'''
x = int(input('x: '))
y = int(input('y: '))
z = int(input('z: '))


if x > z and x > y:
    print(x)
elif y > x and y> z:
    print(y)
elif z > x and z > y:
    print(z)
elif x == z and x > y:
    print (x)
elif y == z and y > x:
    print (y)
elif x == y and x>z:
    print(x)
else:
    print(z)
'''

# @@@@  @@@@@@@ @@@@     15 X, y, z - reprezintă unghiurile unui triunghi
# Verifică și afișează dacă triunghiul este valid sau nu.

'''
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

if a + b + c == 180:
    print ('valid')
else:
    print ('invalid')
'''
