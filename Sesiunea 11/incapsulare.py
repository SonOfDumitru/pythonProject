'''
trei tipuri de metode si atribute:

-public  -> accesibile peste tot
-private -> accesibile doar in clasa (__atribute)
-protected -> accesibil doar in ierarhia de mostenire (_atribute)

'''


class Car:
    __model = 'Dacia'

    def get_model(self):  # getter pentru a return modelul
        return self.__model

    def set_model(self, value):  # setar pentru a schimba valoarea curenta din model
        self.__model = value


c = Car()
print(c.get_model())

c.set_model('volvo')
print(c.get_model())


class Plane:
    __color = 'red'
    @property  #functioneaza ca si un getter
    def color(self):
        print('setting as property')
        return self.__color
    @color.getter
    def color(self):
        print('Getting value')
        return self.__color
    @color.setter
    def color(self,value):
        print('Setting value')
        self.__color=value
    @color.deleter
    def color(self):
        print('delete')
        self.__color=None

    @property
    def is_painted(self):
        return self.__color is not None

p=Plane()
print(p.color)
p.color='blue'
print(p.color)
del p.color
print(p.color)
print(p.is_painted)
