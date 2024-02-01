from abc import ABC, abstractmethod
from pprint import pprint


class Gradinita(ABC):
    @abstractmethod
    def activitate_practica(self):
        pass

    @abstractmethod
    def ora_de_somn(self):
        raise NotImplementedError


class GradinitaPublica(Gradinita):
    def activitate_practica(self):
        print('Copiii invata sa deseneze')

    def ora_de_somn(self):
        print('Copiii trebuie sa doarma la ora 5')


class GradinitaPrivata(Gradinita, ABC):  # ABC este pus pentru ca nu sunt "activate" ambele functii din clasa abstract si sa fie mai evident
    __elevi = {}

    def _adauga_elev(self, **kwargs):
        self.__elevi.update(kwargs)

    @property
    def elevi(self):
        return self.__elevi

    @elevi.setter
    def elevi(self, value):
        self._adauga_elev(**value)



    def activitate_practica(self):
        print("Copiii invata sa modele cu plastelina")


class GradinitaPrivata11(GradinitaPrivata):
    def ora_de_somn(self):
        print('Copiii dorm intre 1 si 2 ')

class GradinitaPublica25(GradinitaPublica):
    nr_elevi = 600   #atribut public
    _adresa = 'str.Napoca 12'   #atribut protected
    __fonduri = 300_000    #atribut privat
    @property
    def fonduri(self):
        return self.__fonduri

    @fonduri.setter
    def fonduri(self, value):
        self.__fonduri = value

    @fonduri.deleter
    def fonduri(self):
        self.__fonduri = None

    def activitate_practica(self):
        print("Copiii se joaca in curte pe balansoare")

    def calc_medie_buline(self, buline):
        medie = sum(buline) / len(buline)
        if medie > 5:
            print('Elevii acestei gradinite sunt foarte neastamparati.')

    def info_elevi(self):
        elevi = {}
        while True:
            nume_elev = input('Nume elev: ')
            nume_parinti = input('Nume parinti: ')
            varsta = input('Varsta elev: ')
            activitate_preferata = input('Activitate preferata elev: ')
            elevi[nume_elev] = {
            'nume_parinti' : nume_parinti,
            'varsta' : varsta,
            'activitate_preferata' : activitate_preferata
            }
            introduce = input('Doresti sa introduci date in continuare(y/n): ')
            if introduce.lower != 'y':
                break

        pprint(elevi)


p = GradinitaPublica()
p.activitate_practica()

# pr = GradinitaPrivata() -> da eroare pentru ca nu se pot crea obiecte pentru clase abstracte
p25 = GradinitaPublica25()
p25.activitate_practica()
p25.ora_de_somn()
p25.calc_medie_buline([1, 2, 3, 6, 8, 9, 4, 5])
p25.calc_medie_buline([12, 10, 8, 9, 4, 5])
#p25.info_elevi()

print(p25.nr_elevi)
print(p25.fonduri)
p25.fonduri = 200_000
print(p25.fonduri)

pr11 = GradinitaPrivata11()
pr11.elevi = {'Andrei':{'varsta':3, 'an_inscriere': 2022}}
pr11.elevi = {'Valentina':{'varsta':2, 'an_inscriere': 2023}}
print(pr11.elevi)
