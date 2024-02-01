# 1.Funcție care să calculeze și să returneze suma a două numere

def sum_two_numbers(a, b):
    return a + b


s = sum_two_numbers(3, 4)
print(s)


# 2. Funcție care să returneze TRUE dacă un număr este par, FALSE pentru impar

def even_number(c):
    if c % 2 == 0:  # return c%2==0
        return True


print(even_number(1665))


# 3. Funcție care returnează numărul total de caractere din numele tău complet.
# (nume, prenume, nume_mijlociu)

def full_name_len(first_name, last_name, middle_name):
    return len(first_name + last_name + middle_name)


print(full_name_len("sorin", "dan", "ailenei"))


# 4. Funcție care returnează aria dreptunghiului (Lungime * latime)

def aria_dreptunghi(L, l):
    return l * L


print(aria_dreptunghi(3, 6))

# 5. Funcție care returnează aria cercului (Pi * r^2)

import math


def aria_cerc(radius):
    return math.pi * radius ** 2


print(aria_cerc(6))


# 6. Funcție care returnează True dacă un caracter x se găsește într-un string dat și False dacă nu găsește.

def is_char_in_str(x, text):
    return x in text


print(is_char_in_str('s', "Sorin s-a dus la plisbare"))
print(is_char_in_str('x', "Sorin s-a dus la plimbare"))

# 7. Funcție fără return, primește un string și printează pe ecran:
# Numărul de caractere lower case este x
# Numărul de caractere upper case exte y
'''
def lower_upper(text):
    count_lower = 0
    count_upper = 0
    for char in text:
        if char.islower():
            count_lower += 1
        elif char.isupper():
            count_upper += 1


print(f'numar de char lower este {count_lower}')
print(f'numar de char upper este {count_upper}')

lower_upper("Ana Are Mere")
'''


# 8. Funcție care primește o LISTĂ de numere și returnează o LISTĂ doar cu numerele pozitive.

def get_all_positives(number):
    resolve_positive = []
    for elem in number:
        if elem > 0:
            resolve_positive.append(elem)
        return resolve_positive


print(get_all_positives([1, 2, 3, 4, 5, -6]))


# 9. 9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZĂ
# Primul număr x este mai mare decat al doilea număr y
# Al doilea număr y este mai mare decat primul număr x
# Numerele sunt egale.

def compare(x, y):
    if x > y:
        print(f'Primul număr {x} este mai mare decat al doilea număr {y}')
    elif x < y:
        print(f'Al doilea număr {y} este mai mare decat primul număr {x}')
    else:
        print('Numerele sunt egale.')


compare(12, 11)
compare(12, 31)
compare(31, 31)


# 10.1 Funcție care primește un număr și un set de numere.
# Printează ‘am adaugat numărul nou în set’ + returnează True
# Printează ‘nu am adaugat numărul în set. Acesta există deja’ + returnează False

def is_number_added_in_set(nr, numbers):
    if nr in numbers:
        print('nu am adaugat numărul în set. Acesta există deja')
        return False
    else:
        numbers.add(nr)
        print('am adaugat numărul nou în set')
        return True


print(is_number_added_in_set(6, {1, 2, 4, 7, 8, 9, }))

# 11. Funcție care primește o lună din an și returnează câte zile are acea lună.

from calendar import monthrange
from datetime import datetime, timedelta


def days_in_month(month):
    year = datetime.today().year
    #   return monthrange(year,month)[1]
    weekday, month_days = monthrange(year, month)
    return month_days


print(days_in_month(9))
print(days_in_month(2))


# 12. Funcție calculator care să returneze 4 valori. Suma, diferența, înmulțirea, împărțirea a două numere.

def calculator(a, b):
    return a + b, a - b, a * b, a / b


a, b, c, d = calculator(10, 2)
print("Suma: ", a)
print("Diferenta: ", b)
print("Inmultirea: ", c)
print("Impartirea: ", d)


#13. Funcție care primește o listă de cifre (adică doar 0-9)
#Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
#Returnează un DICT care ne spune de câte ori apare fiecare cifră
#=> dict {
# 0: 0
# 1 :2
# 2: 0
# 3: 1
# 4: 0
# 5: 3
# 6: 0
# 7: 2
# 8: 0
# 9: 1
# }

def count_digits(digits):
    dct = {}
    for i in range(10):
        dct[i]=0 #setam numarul de aparitii al fiecarei cifre la 0
    for elem in digits:
       # if elem in dct:
            dct[elem]+=1
        #else:
        #    dct[elem]=1
    return dct
print(count_digits([1, 3, 1, 5, 9, 7, 7, 5, 5]))


#14. Funcție care primește 3 numere. Returnează valoarea maximă dintre ele.

def maximum(x,y,z):
    return max(x,y,z)

print(maximum(5,6,8))

#15. Funcție care să primească un număr și să returneze suma tuturor numerelor de la 0 la acel număr.
#Exemplu: dacă dăm numărul 3, suma va fi 6 (0+1+2+3)

def sum_until_nr(nr):
    s=0
    for x in range(nr+1):
        s+=x
    return s
print(sum_until_nr(6))
print(sum_until_nr(3))

# 16.Funcție care primește 2 liste de numere (numerele pot fi dublate). Returnați numerele comune.
#
# Exemplu:
# list1 = [1, 1, 2, 3]
# list2 = [2, 2, 3, 4]
# Răspuns: {2, 3}

def common_numbers(lst1,lst2):
    return set(lst1) & set(lst2) #intersectie
print(common_numbers(lst1 = [1, 1, 2, 3],lst2 = [2, 2, 3, 4]))


#17. Funcție care să aplice o reducere de preț.
#Dacă produsul costă 100 lei și aplicăm reducere de 10%. Pretul va fi 90 de lei.
#Tratează cazurile în care reducerea e invalidă. De exemplu o reducere de 110% e invalidă.

def apply_discount(price, discount):
    if 0<=discount<=100:
        return price - price*discount/100
    print('reducerea aplicata nu este valida')
print(apply_discount(100, 110))

#  18.Funcție care să afișeze data și ora curentă din România.
# (bonus: afișazăi și data și ora curentă din China)

def current_datetime():
    now=datetime.now()
    print(f'Romania {now}')
    print(f'China {now + timedelta(hours= 6)}')
current_datetime()


#19. Funcție care să afișeze câte zile mai sunt până la ziua ta / sau până la Crăciun dacă nu vrei să ne zici cand e ziua ta :)

def days_until_Christmas():
    christmas_date_string = '25.12.2023'
    christmas_date = datetime.strptime(christmas_date_string, '%d.%m.%Y')
    today = datetime.today()
    return (christmas_date - today).days
print(days_until_Christmas())
