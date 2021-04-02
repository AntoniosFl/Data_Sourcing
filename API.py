import requests


def search_city(query):

    url = f"https://www.metaweather.com/api/location/search/?query={query}"
    cities = requests.get(url).json()
    if len(cities) == 0:
        print("Sorry, I don't know this city.")
        return None
    if len(cities) == 1:
        return cities[0]
    for i, city in enumerate(cities):
        print(f"{i+1}.{city['title']}")
        index = int(input('Which one did you mean?'))-1
        return cities[index]
