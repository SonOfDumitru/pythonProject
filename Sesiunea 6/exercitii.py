'''
Sa se scrie un program care citeste numere de la tastatura pana cand se introduce numarul 0.
Pentru fiecare numar introdus se verifica daca este par, iar la final se vor afisa intr-o lista toate numerele pare.
'''

'''
x = -1
rezultat = []

while x:  # X!=0 adica diferit dar prescutat
    x = int(input('introdu un numar: '))
    if x % 2 == 0:
        rezultat.append(x)
    print(rezultat)
'''

'''
Sa se scrie un program care citeste un text de la tastatura si va afisa un dictionar cu toate caracterele din text 
in care cheile vor fi caracterele, si valorile daca caracterul cheie este vocala sau consoana.
'''
'''
dic = {}
text = input('introdu un text: ')
for char in text:
    if not char.isalpha():
        continue
    char_type = 'vocala' if char.lower() in 'aeiou' \
    else 'consoana'
    dic[char] = char_type
print(dic)
'''
'''
1.Având lista:
mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel'] 

Folosește un for că să iterezi prin toată lista și să afișezi;
‘Mașina mea preferată este x’.
Fă același lucru cu un for each.
Fă același lucru cu un while.

'''
# 1.1
'''
import random

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']

print(f'Masinea mea este', (random.choice(masini)))
'''
# 1.2
'''
import random

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']


for x in masini:
    if x == random.choice(masini):
            print('Masina mea preferata este', x)
    else:
        continue
'''

# 1.3
'''
import random

count = 0
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
print(random.choice(masini))

while count < len(masini):
    count = +1
    print(random.choice(masini), 'este masina mea preferata')
    break
'''

'''
2. Aceeași listă:
Folosește un for else
În for
Modifică elementele din listă astfel încât să fie scrise cu majuscule, exceptând primul și ultimul.
În else:
  Printează lista.
'''
'''
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']

result_list = [masini[0]]  # Keep the first item as is

for item in masini[1:8]:
    result_list.append(item.upper())
result_list.append(masini[-1])  # Keep the last item as is  si foarte important locul de unde incepe linia de cod (adica margine de data asta)

print(result_list)
'''

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
'''
masini = ['Audi', 'Volvo', 'BMW', 'Mercede', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
cumparator_doreste = 'Mercedes'
import random
for i in masini:
    if i == cumparator_doreste:
        print('am gasit masina')
        break
else:
    print(f'am gasit masina {random.choice(masini)} mai cautam')
'''

'''

Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu excepția Trabant și Lăstun. 

Dacă mașina e Trabant sau Lăstun:
   Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie else).
Printează S-ar putea să vă placă mașina x.
'''




masini = ['Audi', 'Volvo', 'BMW', 'Mercede', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
cumparator=True

for i in masini:
    if i in ['Trabant','Lăstun']:
        continue
    print(f'S-ar putea să vă placă mașina {i}')
if not cumparator:
    print(f'acestea sunt optiunille {masini}')
