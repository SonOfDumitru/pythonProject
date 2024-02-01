# Json = javascript object notation

from pprint import pprint

import json


def read(filename):
    with open(filename, 'r') as f:
        return json.load(f)


pprint(read('anagajati.json'))

'''
def write(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent = 4)

data = [
   {"Nume": "Dragos", "Varsta": "24"},
   {"Nume": "Andrei", "Varsta": "31"},
   {"Nume": "Dan", "Varsta": "22"},
   {"Nume": "Ioana", "Varsta": "20"}
]

write('indivizi.json', data)
'''
