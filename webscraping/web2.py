import requests

url = "https://jsonplaceholder.typicode.com/comments"
params = {
    'postId':  1,
  }
response = requests.get(url = url, params=params)

print(response.text)