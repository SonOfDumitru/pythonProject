from pprint import pprint

import requests

URL = 'https://jsonplaceholder.typicode.com/'
response = requests.get(f'{URL}/posts')

if response.status_code == 200:  # Daca requestul a avut succes
    data = response.json()  # Transformam continutul din corpul raspunsului din string formatat json intr-un dictionar
    pprint(data)
else:
    print('Request failed with status code: ', response.status_code)
