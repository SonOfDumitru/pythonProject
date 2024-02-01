from pprint import pprint

import requests

URL = 'https://jsonplaceholder.typicode.com'

payload = {
    'title': 'new title'
}

response = requests.patch(f'{URL}/posts/1', json=payload)

if response.status_code == 200:
    data = response.json()
    pprint(data)
else:
    print('Request failed with status code: ', response.status_code)

'''
Patch modifica doar campurile specificate in payload
'''
