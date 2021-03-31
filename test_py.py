import requests

r = requests.get('https://covid19.gov.gr/covid19-live-analytics/')

print(r.status_code)

print('vs code branch testing')
