destinatii = ['nepal', 'canada', 'argentina', 'islanda', 'dolomiti', 'portugalia']
numere = [1, 2, 3, 4, 5, 6, 7, 8, 9]

'''
#Access List Elements: Print the first and last elements of the list you created.

x  =  destinatii[0]
y  =  destinatii[-1]

print(x,y)

#List Slicing: Print the first three elements of the list.

destinatii = destinatii[0:3]
print(destinatii)

#List Length: Find and print the number of elements in your list.

destinatii = ['nepal', 'canada', 'argentina', 'islanda', 'dolomiti', 'portugalia']
x = len(destinatii)
print(x)

#Append and Extend: Add a new fruit to your list using both append() and extend() methods.
destinatii.append('India')
print(destinatii)

destinatii.extend(numere)
print(destinatii)

#Remove an Item: Remove a fruit from your list using the remove() method.
destinatii = ['nepal', 'canada', 'argentina', 'islanda', 'dolomiti', 'portugalia']

destinatii.remove('canada')
print(destinatii)

x = destinatii.pop(2)
print(x)
print(destinatii)

#Insert an Item: Insert a fruit at a specific position in the list using the insert() method.

destinatii.insert(3,'spania')
print(destinatii)
'''
# Sort the List: Sort your list in alphabetical order using the sort() method.

destinatii.sort(reverse=True)
print(destinatii)

destinatii = sorted(destinatii, key=len)  # sorteaza in functie de lungimea fiecarui element in parte
print(destinatii)

# Reverse the List: Reverse the order of your list using the reverse() method.
destinatii = ['nepal', 'canada', 'argentina', 'islanda', 'dolomiti', 'portugalia']

destinatii.reverse()
print(destinatii)

# Check for an Item: Check if a specific fruit is in your list using the in keyword.
x = 'canada'


if x in destinatii:
    print(f'{x} e in lista')

# Count Occurrences: Count how many times a specific fruit appears in your list using the count() method.

destinatii = ['nepal', 'canada', 'argentina', 'islanda', 'dolomiti', 'portugalia','canada','canada']
print(destinatii.count('canada'))

# Iterate Over a List: Use a for loop to print each fruit in your list.

# List Comprehension: Create a new list that contains the lengths of each fruit name in your original list using list comprehension.

# Copy a List: Create a copy of your list using both the copy() method and the slicing [:] method.

# Clear a List: Remove all elements from your list using the clear() method.

# Join Lists: Create a new list by combining your fruit list with a list of vegetables.

# Nested Lists: Create a list of lists to represent a simple 2D grid.

# List Methods: Experiment with other list methods like pop(), index(), and sort().

# List as a Stack: Implement a simple stack (Last-In-First-Out) using a list. Push and pop items.

# List as a Queue: Implement a simple queue (First-In-First-Out) using a list. Enqueue and dequeue items.


# Funcție pentru calcularea mediei aritmetice a unei liste de numere:

def media_aritmetica(numere):
    suma = sum(numere)
    numar_elem= len(numere)
    media = suma/numar_elem
    return media

list_numere = [float(input(f"Introduceți numărul {i}: ")) for i in range(5)]

rezultat = media_aritmetica(list_numere)
print(input(f' Media este: {rezultat}'))


name = input('Care e numele tau? ')
print('salut ' + name)
color = input('Si care e culoarea ta preferata? ')
print('Culoarea mea preferata este ' + color)


