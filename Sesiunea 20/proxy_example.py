'''
proxy este un sablon structural care te lasa sa oferi un substitut pt un alt obiect.
o clasa proxy controleaza accesul la obiectul original  permitand niste actiuni
inainte sau dupa ce se realizeaza actiunea obiectului original.
Avantaje:
- poti controla obiectul original fara ca cei care il folosesc sa stie detalii despre acesta
- poti gestiona ciclul de viata al obiectului original fara a afecta clasele care il utilizeaza
- clasa proxy functioneaza si daca obiectul original nu este pregatit sau nu este disponibil
Dezavantraje:
- codul poate deveni mai complicat deoarece ste nevoie de introducerea mai multor clase
- raspunsul de la obiectul original poate fi intarziat din cauza clasei proxy
'''

from abc import ABC, abstractmethod


class Subject(ABC):
    @abstractmethod
    def request(self):
        pass


class RealSubject(Subject):
    def request(self):
        print('real subject: ma ocup de request')


class Proxy(Subject):
    def __init__(self, rs):
        self.realsubject = rs

    def check_access(self):
        print('proxy:verificam access pt request')
        return True

    def log_request(self):
        print('proxy:se afiseaza timpul requestului')

    def request(self):
        if self.check_access():
            self.realsubject.request()
            self.request = self.log_request()


rs = RealSubject()
rs.request()
print(50 * '*')

proxy = Proxy(rs)
proxy.request()
