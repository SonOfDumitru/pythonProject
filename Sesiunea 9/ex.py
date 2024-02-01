# 1.Funcție care să calculeze și să returneze suma a două numere

def sum_2_numbers(a, b):
    return a + b

print(sum_2_numbers(10 , 13 ))
print(sum_2_numbers(-1 , 13 ))

#
# 2. Funcție care să returneze TRUE dacă un număr este par, FALSE pentru impar

def is_even(nr):
    if nr%2==0:
        return True
    return False
print(is_even(7))
print(is_even(8))
print(is_even(-1))


# 3. Funcție care returnează numărul total de caractere din numele tău complet.
# (nume, prenume, nume_mijlociu)

def name_len(nume,prenume,nume_mijlociu):
    x = len(nume+prenume+nume_mijlociu)
    return x
print(name_len("Sorin", "Dumitru", "Ailenei"))

# 5. Scrieţi o funcţie care returnează prima cifră a unui număr natural. De exemplu, dacă parametrul efectiv este 127,
# funcţia va returna 1.

def first_number( nr):
    nr_str = str(nr)
    if nr_str:
        return int(nr_str[0])

print(first_number(2345))



# 6. Să se tipărească toate numerele prime aflate între doi întregi citiţi. Programul va folosi o funcţie care testează
# dacă un număr este prim sau nu.
#
# 7. Scrieţi un program care tipăreşte numerele întregi găsite între două valori citite, numere care se divid cu suma cifrelor lor.
# Programul va utiliza o funcţie care returnează suma cifrelor unui număr întreg primit ca parametru.
