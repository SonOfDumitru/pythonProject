class Dog:
    def __init__(self,age,name):  #constructor
        self.name = name          #constructor
        self.age = age              #constructor
    def bark(self):
        print ('woof')
    def print_name(self):
        print(self.name)
    def print_age(self):
        print(self.age)

d = Dog(4, 'Henry')
d.bark()
d.print_name()
d.print_age()

