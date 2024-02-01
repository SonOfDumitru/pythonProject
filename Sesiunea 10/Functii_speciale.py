class Dog:
    def __init__(self, age, name):
        self.name = name
        self.age = age

    def __str__(self):
        return f'varsta: {self.age}, nume: {self.name}'

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if not isinstance(other, Dog):
            return False
        return self.name == other.name


d = Dog(1, 'Bolt')
print(d)
d2 = Dog(2, 'Volt')
print(d, d2)
d3 = Dog(2, 'Volt')
print(d2 == d3)
print(d3 == 7)
