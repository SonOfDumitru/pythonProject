'''
1. Alege un user din lista de useri predefiniti. Pentru acesta, fa requesturile necesare pentru a afișa următoarele informații:
	-> lista de posts
Pentru a menține output-ul la un nivel acceptabil, afișează la fiecare dintre aceste liste doar informații despre primele 3 obiecte,
iar apoi afiseaza "+x more posts/", unde x este numărul de obiecte rămase.

'''
from pprint import pprint

import requests


class PostsAPIClient:
    URL = 'https://jsonplaceholder.typicode.com'
#rez 1
    def get_posts_by_user(self, userId):
        response = requests.get(f'{self.URL}/posts?userId={userId}')
        posts = response.json()
        first_3 = posts[:3]
        return first_3, len(posts) - 3
#rez 2
    def get_comments_by_post(self, postId):
        response = requests.get(f'{self.URL}/comments?postId={postId}')
        return response.json()

#rez 3
    def create_post(self, new_post):
        response = requests.post(f'{self.URL}/posts', json=new_post)
        return response.json()
#rez 5
    def get_todo_by_user(self, userId):
        response = requests.get(f'{self.URL}/todos?userId={userId}&completed=false')
        return response.json()

client = PostsAPIClient()
posts, left = client.get_posts_by_user(97)

pprint(posts)
print(f'+{left} more posts/')

'''
2. Alege un post, și afișează lista de comentarii. Alege un album, si afiseaza lista de photos.
'''
#rez 2
pprint(client.get_comments_by_post(100))

'''
3. Creeaza un post nou (atentie, acesta NU va fi salvat, dar putem analiza răspunsul
pentru a vedea cum ar arata în viitor dacă ar fi fost salvat). Încearcă să-l creezi cu si fără id. Ce observi?
'''
#rez 3
payload = {
    'title': 'new title',
    'body': 'new body',
    'userId': 3
}
pprint(client.create_post(payload))

'''
5. Folosind query parameters,
filtrează lista de todos pentru userul ales astfel incat sa afisezi doar todos care nu sunt completed.
'''
pprint(client.get_todo_by_user(1))
