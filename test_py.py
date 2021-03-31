import requests

r = requests.get('https://www.e-radio.gr/category/sports')

print(r.status_code)
