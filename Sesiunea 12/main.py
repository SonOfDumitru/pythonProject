# from dog import Dog   #import doar clasa din fisier
# from chiuaua import Chiuaua
#
# d= Dog()
# c = Chiuaua()
#
# d.bark()
# c.bark()

# import dog #imporatarea intregului fisier/modul dog
# import chiuaua
#
# d= dog.Dog      #arata ca vrem sa folosim clasa Dog din fierul dog
# c= chiuaua.Chiuaua

# import dog as D #importarea intregului modul doc si redenumire in D
# import chiuaua as C
#
# d = D.Dog     # se importat sub denumirea data mai sus
# c= C.Chiuaua

from dog import *   # a nu sw folosi pt ca poate crea confuzie
from chiuaua import *  # a nu sw folosi pt ca poate crea confuzie

d = Dog()
c = Chiuaua()
