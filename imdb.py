from bs4 import BeautifulSoup
import requests

url = 'https://www.imdb.com/list/ls055386972/'

response = requests.get(url, headers={'Accept-Language': 'en-US'})

soup = BeautifulSoup(response.content, 'html.parser')

movies = []

movie_html = soup.find_all('div', class_='lister-item-content')
for movie in movie_html:
    title = movie.find('h3').find('a').string
    duration = movie.find('span', class_='runtime').string
# or duration = movie_html.find('span', class_='runtime').string.strip('min')
# duration = duration.split()
# print(duration[0])
    duration = ''.join(i for i in duration if i.isdigit())
    movies.append({'title': title, 'duration': duration})
# def parse(html):
#   response = requests.get(url)
#   soup = BeautifulSoup(response.content, 'html.parser')
print(movies[0:6])
