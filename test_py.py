import requests
import ipdb

url = "https://www.metaweather.com/api/location/search/?query=london"
response = requests.get(url).json()
ipdb.set_trace()
city = response[0]
print(f"{city['title']}: {city['woeid']} ({city['latt_long']})")
