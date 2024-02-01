# 1. Sa se scrie un program care citeste un text de la tastatura si afiseaza o lista cu fiecare caracter in ordinea inversa
# a aparitiei in text.
'''
text = input('introdu cuvant:')
l = list(text)
print(l[::-1])
'''
# 2. 2. Sa se scrie un program care citeste numele, emailul si varsta unei persoane de la tastatura si adauga toate datele intr-un dictionar pe care il afiseaza.
# Daca persoana nu este multumita cu datele introduse va putea specifica daca vrea sa modifice maxim o valoare din dictionar.

'''
nume = input('introdu numele:')
mail = input('introdu mail:')
varsta = int(input('introdu varsta:'))

data = {
    'nume': nume,
    'varsta': varsta,
    'mail': mail
}

print(data)

modifica = input('vrei sa modifici datele?(y/n): ')

if modifica == 'y':
    cheie_de_modificat = input(' ce doresti sa modifici')
    if cheie_de_modificat not in data:
        print('nu exista aceasta valoare')
    else:
        valoare_de_modificat = input('introdu noua valoare:')
        valoare_de_modificat = int(valoare_de_modificat) if cheie_de_modificat == 'varsta' else valoare_de_modificat
        data[cheie_de_modificat] = valoare_de_modificat
print(data)
'''

'''
12. Ne imaginăm o echipă de fotbal pt teren sintetic.
3 Schimbări maxime admise:

Declară o Listă cu 5 jucători
Schimbari_efectuate = te joci tu cu valori diferite
Schimbari_max = 3

Dacă Jucătorul x e în teren și mai avem schimbări la dispoziție
Efectuează schimbarea 
Șterge jucătorul scos din listă
Adaugă jucătorul intrat
Afișază a intrat x, a ieșit y, mai ai z schimbări

Dacă jucătorul nu e în teren:
Afișează ‘nu se poate efectua schimbarea deoarece jucătorul x nu e în teren’
Afișează ‘mai ai z schimbări’

Testează codul cu diferite valori

Google search hint
“how to check if item is în list python”
'''

jucatori = ['vio', 'joe', 'bo', 'luie', 'so']
print(jucatori)

nume_jucator = input('nume jucator: ')
schimbare = int(input('introdu nr schimbair ramase '))
x = (nume_jucator is jucatori)

if schimbare < 3:
    if nume_jucator in jucatori:
        jucatori[x] = 'flo'
        print(jucatori, 'e pe teren')
    elif nume_jucator not in jucatori:
        print('nu e pe teren')
else:
    print(' ai ramas fara schimbar: ')

        # nume_jucator.remove(3)
        # jucatori[1] = 'flo'
        # print(jucatori)
        # jucatori.pop(nume_jucator) and jucatori.append('Flo'))
        # print(jucatori)


'''
3. Fie seturile:
    
    set1 = {"Yellow", "Orange", "Black"}
    set2 = {"Orange", "Blue", "Pink"}
    
    
    1. Sa se afiseze toatele elementele care apar in `set1` si nu apar in `set2`
    2. Sa se afiseze toatele elementele care apar in ambele seturi
    3. Sa se afiseze toatele elementele care nu sunt comune
    '''

set1 = {"Yellow", "Orange", "Black"}
set2 = {"Orange", "Blue", "Pink"}

print(set1 & set2)
print(set1 | set2)
print(set1 ^ set2)
