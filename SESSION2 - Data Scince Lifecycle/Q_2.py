"""
2.  Use the requests library in Python to fetch the latest 5 posts from the JSONPlaceholder API 
   (https://jsonplaceholder.typicode.com/posts) and print the title of each post.
   <br><br><em><strong>Hint:</strong> Use requests.get() and response.json().</em>
"""


import requests

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

posts = response.json()

for post in posts[-5:]:
    print(post["title"])