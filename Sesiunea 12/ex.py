'''
1. Clasa Angajat
     Atribute: nume, prenume, salariu
     Constructor pentru toate atributele
     Metode:
descrie()
nume_complet()
salariu_lunar()
salariu_anual()
marire_salariu(procent)


 2. Clasa Factură
     Atribute: seria (va fi constantă, nu trebuie constructor, toate facturile vor avea aceeași serie), număr, nume_produs, cantitate, pret_buc
     Constructor: toate atributele, fără serie
     Metode:
schimbă_cantitatea(cantitate)
schimbă_prețul(pret)
schimbă_nume_produs(nume)
generează_factura() - va printa tabelar dacă reușiți

Factura seria x număr y
Data: generează automat data de azi
Produs | cantitate | preț bucată | Total
Telefon |      7       |       700       | 49000

Indiciu pentru dată: https://www.geeksforgeeks.org/get-current-date-using-python/
'''

import datetime

class Angajat():
    def __init__(self, nume , prenume,  salariu, an_angajare):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu
        self.an_angajare = an_angajare

    def nume_complet(self):
        print(f'Numele complet al angajatului este {self.nume} {self.prenume}')

    def salariu_lunar(self):
        print(f'Salariul lunar al angajatului este {self.salariu} ')

    def salariu_anual(self):
        salariu_anual =  self.salariu * 12
        print(f'Salariul anual al angajatului este {salariu_anual} ')
        return salariu_anual

    def marire_salariu(self,  an_curent):
        v = an_curent - self.an_angajare
        procent = v * 5  # 5% increase for every year of employment

        salariu_nou = self.salariu * (1 + procent / 100)
        print(f'Marirea de salariu a angajatului este {procent}%, rezultând salariul nou de {salariu_nou}')
        return salariu_nou



# Get the current year
current_year = datetime.datetime.now().year

# instanta Angajat
a = Angajat('Tom', 'Jones', 10000, an_angajare=2018)
# Call the methods
a.nume_complet()
a.salariu_lunar()
a.salariu_anual()

# Example of increasing salary based on years of employment
a.marire_salariu(an_curent=current_year)


from datetime import date

class Factura:
    seria = 745632

    def __init__(self, numar , nume_produs,  cantitate, pret_buc):
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_buc = pret_buc

    def schimba_cantitatea(self):
        new_cantitate = int(input(f'Introdu cantitatea curentă {self.cantitate}: '))
        self.cantitate = new_cantitate


    def schimba_pretul(self):
        new_pret = float(input(f'Introdu prețul curent {self.pret_buc}: '))
        self.pret_buc = new_pret


    def schimba_nume_produs(self):
        new_nume = input(f'Introdu noul nume de produs pentru "{self.nume_produs}": ')
        self.nume_produs = new_nume

    def genereaza_factura(self):
        numar_factura = int(input('Introdu numărul facturii: '))
        if numar_factura > 0:
            print(f'Factura seria: {self.seria}, numărul {numar_factura}')

        today = date.today()
        print(f'Data: {today}')

        self.total = self.cantitate * self.pret_buc
        print(f"\nProdus | Cantitate | Preț/bucată | Total")
        print("-" * 40)
        print(f"{self.nume_produs} | {self.cantitate} | {self.pret_buc} | {self.total}")




f = Factura(0,'telefon',0 , 100 )

f.schimba_cantitatea()
f.schimba_pretul()
f.schimba_nume_produs()
f.genereaza_factura()

