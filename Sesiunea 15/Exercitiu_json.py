'''
a) Sa se scrie o functie care citeste datele din fisierul `employees.json`.

b) Sa se creeze o functie care afiseaza toti angajatii care au mai putin de 5 zile de concediu medical

'''
import json
from pprint import pprint


def read(filename):
    with open(filename,'r') as f:
        return json.load(f)


pprint(read('employes.json'))


def read_filtered(filename):
    data =read(filename)
    for employee in data:
        if employee['sick_days_remaining']<10:
            print(employee)

read_filtered('employes.json')
