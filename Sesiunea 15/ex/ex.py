import csv
import json
from pprint import pprint
from tabulate import tabulate


def read_csv(filename):
    with open(filename,'r') as f:
        reader = csv.reader(f)
        return list(reader)
        
def table(data):
    headers, *rows = data
    table = tabulate(rows, headers=headers)
    print(table)
    
def read_json(filename):
    with open(filename, 'r') as f:
        return json.load(f)
        
def write_json(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f)

students = read_csv('students.csv')

table(students)
'''
students_json = [
   {
		"id": int(id),
		"fname": fname,
		"lname": lname,
		"age": int(age),
		"grade": float(grade)}
        for id, fname, lname, age, grade in students[1:]]

pprint(students_json)
new_data = [
    {
        "id": 7,
        "fname": "Alex",
        "lname": "Smith",
        "age": 28,
        "grade": 9.2
    }
]


write_json('students.json', new_data)
'''
