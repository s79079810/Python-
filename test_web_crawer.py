import requests
r = requests.get('https://www.google.com.tw/')
print(r.text)