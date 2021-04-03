from bs4 import BeautifulSoup
import requests


def parse(ingredient):

    base_url = f"https://recipes.lewagon.com/?search[query]={ingredient}"

    response = requests.get(base_url)

    soup = BeautifulSoup(response.content, 'html.parser')

    receipes = []

    receipes_html = soup.find_all('div', class_='p-2 recipe-details')
    for receipe in receipes_html:
        name = receipe.find(
            'p', class_='text-dark text-truncate w-100 font-weight-bold mb-0 recipe-name').string
        difficulty = receipe.find('span', class_='recipe-difficulty').string
        prep_time = receipe.find(
            'span', class_='recipe-cooktime').string.split()[0]

        receipes.append(
            {'title': name, 'difficulty': difficulty, 'cooktime': prep_time})

    return receipes[0:31]
