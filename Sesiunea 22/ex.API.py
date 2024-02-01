from pprint import pprint

import requests


class BooksAPIClient:
    URL = 'https://simple-books-api.glitch.me'

    def __init__(self, client_name, client_email):
        self.client_name = client_name
        self.client_email = client_email
        self._token = '56cac3e768e51c8d16a4c70ff97ac6a4c99e85fa6b809d83ed07debbb0fd76bc' or self.__generate_token()

    def __generate_token(self):
        response = requests.post(f'{self.URL}/api-clients',
                                 json={'clientName': self.client_name, 'clientEmail': self.client_email})
        data = response.json()
        print(data)
        return data.get('accesToken')

    def __get_headers(self):
        return {
            'Authorization': f'Bearer {self._token}'
        }

    def add_order(self, bookId):
        response = requests.post(f'{self.URL}/orders', json={'bookId': bookId, 'customerName': self.client_name},
                                 headers=self.__get_headers())
        return response.json()

    def get_all_orders(self):
        response = requests.get(f'{self.URL}/orders', headers=self.__get_headers())
        return response.json()

    def delete_order(self, orderId):
        requests.delete(f'{self.URL}/orders/{orderId}', headers=self.__get_headers())


b = BooksAPIClient('Rares', 'rares1@gmail.com')

print(b.add_order(1))
pprint(b.get_all_orders())
print('*************' * 2)
b.delete_order('ACawbuW6CO-wlNTVqdn9q')
print('*************' * 2)
pprint(b.get_all_orders())
