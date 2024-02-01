class FileManager:
    def __init__(self, filename, mode):  # open (filename, 'r')
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


with FileManager('data.txt', 'w') as f:
    f.write('test')


from contextlib import contextmanager
@contextmanager

def file_manager(filename,mode):
    f=open(filename,mode)
    yield f
    f.close()

with file_manager('data.txt', 'w') as f:
    f.write('text.2')
