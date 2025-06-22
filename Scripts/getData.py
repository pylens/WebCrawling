import requests

# it sends the http request to the specific url

url = 'https://en.wikipedia.org/wiki/Construction'

content = requests.get(url)
print(content)
print(type(content))
print(content.text)