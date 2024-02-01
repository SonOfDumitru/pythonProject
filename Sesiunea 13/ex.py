class Masina:
    marca = 'Dacia'
    viteza_actuala = 0
    culoare = 'gri'
    culori_disponibile = {'rosu', 'alb', 'verde', 'mov', 'negru'}
    inmatriculata = False

    def __init__(self, model, viteza_maxima):
        self.model = model
        self.viteza_maxima = viteza_maxima

    # descrie() - se vor printa toate atributele, în afară de culori_disponibile
    def descriere(self):
        print(
            f'Fabirca produce {self.marca} in culoarea standard {self.culoare} si se poate customiza in culorile {", ".join(self.culori_disponibile)}')
        if self.inmatriculata:
            print('Masina este inmatriculata.')

    # înmatriculare() - va schimba atributul înmatriculată în True
    def inmatriculare(self):
        self.inmatriculata = True

    # vopsește(culoare) - se va vopsi mașina în noua culoare DOAR dacă noua culoare e în opțiunea de culori disponibile, altfel afișați o eroare
    def vopseste(self):
        culoare_noua = input('Specifica culoarea dorita la masina: ').lower()
        if culoare_noua in self.culori_disponibile:

            print(f'Masina va avea culoarea: {culoare_noua}')
        else:
            print(f'Masina nu poate fi vopsita in culoarea {culoare_noua}')

    # accelerează(viteza) - se va accelera la o anumită viteză, dacă viteza e negativă-eroare, dacă viteza e mai mare decât viteza_max - masina va accelera până la viteza maximă
    def accelereaza(self):
        viteza = int(input('Masina accelereaza pana la viteza '))
        if viteza < self.viteza_maxima:
            print(f'Masina va accelara pana la {self.viteza_maxima}')
        elif viteza == self.viteza_maxima:
            print(f'Masina a atins viteza maxima de {self.viteza_maxima}')
        else:
            print(f'Erroare! Masina nu poate depasi viteza maxima de {self.viteza_maxima}')

# franeaza() - mașina se va opri și va avea viteza 0
    def franeza(self):
        frana = input('Doresti sa opresti masina: y/n ').lower()
        if frana == 'y':
            frana = self.viteza_actuala
            print(f'mașina se va opri și va avea viteza {frana}')
        else:
            print(f'Mașina va continua sa mearga')


m = Masina(model='Logan', viteza_maxima=100)
m.descriere()

m.inmatriculare()

m.vopseste()

m.accelereaza()

m.franeza()

# franeaza() - mașina se va opri și va avea viteza 0
