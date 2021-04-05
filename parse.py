from bs4 import BeautifulSoup
import requests

base_url = f"https://recipes.lewagon.com/"


def parse(ingredient, start=1):
    if start <= max_page(ingredient, start):
        response = ingredient_response(ingredient, start)
        soup = BeautifulSoup(response.text, 'html.parser')
        receipes = []
        receipes_html = soup.find_all('div', class_='p-2 recipe-details')
        for receipe in receipes_html:
            name = receipe.find(
                'p', class_='text-dark text-truncate w-100 font-weight-bold mb-0 recipe-name').string
            difficulty = receipe.find(
                'span', class_='recipe-difficulty').string
            prep_time = receipe.find(
                'span', class_='recipe-cooktime').string.split()[0]
            receipes.append(
                {'title': name, 'difficulty': difficulty, 'cooktime': prep_time})
    else:
        return(f"Arguement 'start' cannot be greater than {max_page(ingredient)}")

    return receipes
