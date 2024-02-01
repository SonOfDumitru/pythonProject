class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_name(self):
        print(f'numele meu este {self.name}')


class Student(Person):
    pass


p = Person('Andrei', 24)
p.print_name()
s = Student('Maria', 27)
s.print_name()


class Worker(Person):
    def __init__(self, name, age, job):
        #Person.__init__(self,name,age)
        super().__init__(name,age) #super este referinta catre clasa parinte
        self.job = job
w = Worker('Ion',25, 'programator')
w.print_name()

