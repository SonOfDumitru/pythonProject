def product(a, b):
    print(a * b)
product(4,4)

def product(a, b):
    return a * b

p = product(2, 3)
print(p)


def is_even(number):
    # if number % 2 == 0:
    #     return True
    # return False
    return number % 2 == 0
result =is_even(5)
print(result)
result2 =is_even(10)
print(result2)


def get_all_even_numbers(numbers):
    result = []
    for elem in numbers:
        if is_even(elem):  # functie in functie sau elem % 2 == 0: fara a folosi functia de mai sus
            result.append(elem)
    return result


nr = get_all_even_numbers([1, 3, 4, 2, 5, 6, 8, 9])
print(nr)


