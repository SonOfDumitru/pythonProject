from contextlib import contextmanager
@contextmanager

def hello_context_manager():
    print('Intram in context')
    yield 'Hello world'
    print('Iesim din context')

with hello_context_manager() as h:
    print(h)
