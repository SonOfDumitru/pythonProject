'''
print('introduce numar')
x= int(input('x=  '))
y= int(input('y=  '))
z= int(input('z=  '))

s = x +y + z
print(s)

s = x%y
print(s)

s = x // y
print(s)

s= x ** y
print(s)


s = 12
s -= 3  # se pot pune mai multi oepratori de atribuire???
s += 6
print(s)

print ( x > y)
print ( x <= y)
print (x == y)
print (x != y)
print(( 5 < x <10) != 14)
'''

prop = 'introdu test \n'
print(prop)

x = input('')

# convertire la uppercase


# convertire la lowercase


# numar de aparitii si replace si slicing

print((x.count('a')) + (x.count('A')) +(x.count('b')))
print(x.replace('a','so'))
print(x[2:])
print(x[:6])
print(x[3:10])
print(x[2])
print(x.index('a'))

#index - pozitia ordinara a unui caracter


# 9. @@@@ @@@@@ @@@@Citește o literă de la tastatură.
#   Verifică și afișează dacă este vocală sau nu.

ch = input('introdu caracter: ')

if len('ch') == 1:
    if (ch == 'A' or ch == 'a' or ch == 'E' or ch == 'e' or ch == 'I'
            or ch == 'i' or ch == 'O' or ch == 'o' or ch == 'U' or ch == 'u'):
        print(ch, 'e vocala')
    elif ch.isdigit():
        print(ch, 'is a number')
    else:
        print(ch, 'consoana')
else:
    if len(ch) > 1:
        print( 'introdu un caracter')

# 19.Joc ghicit zarul
# Caută pe net și vezi cum se generează un număr random
# Ne imaginăm ca dai cu zarul și salvăm acest număr în dice_roll
# Ia numărul ghicit de la utilizator
# Verifică și afișează dacă utilizatorul a ghicit
# Vei avea 3 opțiuni
# Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y.
# Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y.
# Ai ghicit. Felicitări! Ai ales x si zarul a fost y.



