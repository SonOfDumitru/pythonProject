class EvenIterator:
    def __init__(self,n):
        self.n =  n
        self.generated_number = 0
        self.current_number = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.current_number += 1
        if self.generated_number >= self.n:
            raise StopIteration
        if self.current_number %2 == 0:
            self.generated_number += 1
            return self.current_number
        return self.__next__()

it = EvenIterator(10)
for i in it:
    print(i)
print(50 * '*')

it = EvenIterator(10)

i = next(it)
while i:
    print(i)
    try:
        i = next(it)
    except StopIteration:
        i = None
print(50 * '*')
