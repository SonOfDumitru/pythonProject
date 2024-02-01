class HelloContextManager:
    def __enter__(self):
        print('Intram in context')
        return 'Hello world'

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Iesim din context')
        if exc_type == IndexError:
            print(f'Mesaj de eroare {exc_val}')
            return False   # in acest mod se propaga eroarea in afara contextului, iar daca scriem -
                            # - return True nu se va mai propaga deloc

with HelloContextManager() as h:  #h ia valoarea returnata de functia Enter
    print(h)
    h[100]
print('Nu mai sunt in context')
