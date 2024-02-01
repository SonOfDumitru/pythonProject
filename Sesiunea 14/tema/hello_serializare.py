def read(filename):
    with open(filename, 'r') as f:  # deschidere fisier in mod 'r' (citire) si stocare obiect in variabila f
        return f.readlines()
print(read('hello2.txt'))

def write(filename, data):
    with open(filename, 'w') as f: #deschidere fisier in modul 'w' (write)
        f.writelines(data)
write('hello2.txt',['23\n','94\n','107\n'])  #\n -> linie noua pentru fieca

def append(filename, data):
    with open(filename, 'a') as f:  # deschidere fisier in modul 'a' - append/adaugare
        f.writelines(data)
append('hello2.txt', ['Go\n','Kotlin\n','Swift\n','A\n'])



def append(filename, letter):
    with open(filename, 'w') as f:
        ordinal_suffix = "th" if 11 <= i <= 13 else {1: 'st', 2: 'nd', 3: 'rd'}.get(i % 10, 'th')
        f.write(f"My name is letter {letter}.\n")
        f.write(f"I am the {i}{ordinal_suffix} letter of the alphabet.\n")

for i in range(1, 27):  # ASCII values for A to Z
    letter = chr(i + 64)  # Adjusting ASCII values to start from 'A'
    filename = f"{letter}.txt"
    append(filename, letter)
