def gen_even(n):
    generated_number = 0
    current_number = 0
    while generated_number < n:
        current_number += 1
        if current_number %2 == 0:
            yield current_number
            generated_number += 1

gen = gen_even(10)
for i in gen:
    print(i)
print('*'* 50)

def my_gen():
    n =1
    print('Primul print')
    yield n

    n += 1
    print('Al doilea print')
    yield n

    n += 1
    print('Al treilea print')
    yield n

mg = my_gen()
print(next(mg))
print(next(mg))
print(next(mg))


