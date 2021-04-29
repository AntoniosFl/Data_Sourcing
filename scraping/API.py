import requests
import urllib.parse
import sys

base_url = "https://www.metaweather.com/"


def search_city(city):

    url = urllib.parse.urljoin(base_url, "api/location/search")
    cities = requests.get(url, params={'query': city}).json()
    if len(cities) == 1:
        return cities[0]
    for i, city in enumerate(cities):
        print(f"{i+1}.{city['title']}")
    index = int(input('Which one did you mean?'))-1
    return cities[index]


def weather_forecast(woeid):
    url = urllib.parse.urljoin(base_url, f"/api/location/{woeid}")
    city_id = requests.get(url).json()
    return city_id['consolidated_weather']


def main():
    while True:

        query = input('Pleas.e give me the name of the city:\n>')
        city = search_city(query)
        if not city:
            print("Sorry, I don't know this city.")
        else:
            forecast = weather_forecast(city['woeid'])
            print(f"Here's the weather in {city['title']}:")
            for i in range(len(forecast)):
                print(
                    f"{forecast[i]['applicable_date']}:{forecast[i]['weather_state_name']} {round(forecast[i]['max_temp'])}°C")

            break


if __name__ == '__main__':
    try:
        while True:
            main()
    except KeyboardInterrup:
        print('\nGoodbye')
        sys.exit(0)
