def read(filename):
    with open(filename, 'r') as f:  # deschidere fisier in mod 'r' (citire) si stocare obiect in variabila f
        return f.readlines()
print(read('numere.txt'))


def write(filename, data):
    with open(filename, 'w') as f: #deschidere fisier in modul 'w' (write)
        f.writelines(data)

write('numere2.txt',['8\n','9','10'])  #\n -> linie noua pentru fiecare element scris in fisierul numere2.txt


def append(filename, data):
    with open(filename, 'a') as f:  # deschidere fisier in modul 'a' - append/adaugare
        f.writelines(data)


append('numere.txt', ['1\n', '2\n', '3\n'])
