'''
Sa se scrie o functie care citeste din fisierul persons.csv si adauga la datele din acel fisier o lista de date primita ca parametru.
Rezultatul final va fi scris in fisierul allpersons.csv.
Numele fisierelor vor fi transmise ca parametru.
'''
import csv
from dataclasses import dataclass
from pprint import pprint


@dataclass

class Persons:
    name : str
    age : int
    height: int

    @classmethod # o functie care este atasata clasei nu obiectului; in general folosite pentru alternative in creare obiectelor din aceasta clasa
    def from_dict(cls,dct):
        return cls(dct['name'],int(dct['age']),int(dct['height']))
    def to_dict(self):
        return{'name':self.name,'age':self.age,'height':self.height}

def read(filename):
    with open (filename,'r') as f:
        reader = csv.DictReader(f)
        persons = []
        for row in reader:
            p = Persons.from_dict(row)
            persons.append(p)
        return persons

pprint(read('persons.csv'))


def write(filename, data):
    with open (filename,'w') as f:
        writer = csv.DictWriter(f,fieldnames= ['name','age','height'])
        writer.writeheader()
        for person in data:
            writer.writerow(person.to_dict())

def append(input_filename,output_filename,data):
    persons = read(input_filename)
    persons.extend(data)
    write(output_filename,persons)

PERSONS = [
    Persons("Sergiu", 25, 185),
    Persons("Valentina", 24, 175)
]

write('allpersons.csv',PERSONS)

append('persons.csv','allpersons.csv',PERSONS)

pprint(read('allpersons.csv'))





