
from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    PI = 3.14

    @abstractmethod
    def aria(self):
        pass

# Exemplu de implementare a unei clase concrete
class Cerc(FormaGeometrica):
    def __init__(self, raza):
        self.raza = raza

    def aria(self):
        return self.PI * self.raza**2

# Testare
cerc = Cerc(5)
print(f"Aria cercului: {cerc.aria()}")


class Patrat(FormaGeometrica):
    def __init__(self,latura):
        self.latura = latura

    # Encapsulation - Getter pentru latură
    @property
    def latura(self):
        return self._latura

    # Encapsulation - Setter pentru latură
    @latura.setter
    def latura(self, value):
        if value > 0:
            self._latura = value
        else:
            print("Latura trebuie să fie mai mare decât 0.")

    # Encapsulation - Deleter pentru latură
    @latura.deleter
    def latura(self):
        del self._latura

    def aria(self):
        return self.latura ** 2

patrat = Patrat(7)
print(f'Aria patratului: {patrat.aria()}')
