class CustomException(Exception):
    pass

'''
Sa se scrie o functie care verifica daca o lista de numere intregi contine numere negative
Daca da, sa se arate o exceptie specifica
'''

class ContainsNegativNumberException(Exception):
    pass

def check_neg_numbers(numbers):
    for number in numbers:
        if number < 0:
            raise ContainsNegativNumberException(f'Contine {number}')

check_neg_numbers([1,2,3,4,-2,3,4,5,6])
