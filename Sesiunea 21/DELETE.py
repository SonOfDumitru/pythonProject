from pprint import pprint

import requests

URL = 'https://jsonplaceholder.typicode.com/'
response = requests.delete(f'{URL}/posts/1')
if response.status_code == 200:
    print('Deleted succesfully')
else:
     print('Request failed with status code: ', response.status_code)
