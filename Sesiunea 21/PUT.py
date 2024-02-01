from pprint import pprint

import requests

URL = 'https://jsonplaceholder.typicode.com'

payload = {
    'title': 'new title'
}

response = requests.put(f'{URL}/posts/1', json=payload)

if response.status_code == 200:
    data = response.json()
    pprint(data)
else:
    print('Request failed with status code: ', response.status_code)

'''
PUT modifica intreaga resursa, stergand orice camp nu se afla in paylaodul pe care il trimite la server
'''
