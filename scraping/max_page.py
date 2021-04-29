import sys
import csv
import requests
from bs4 import BeautifulSoup

base_url = f"https://recipes.lewagon.com/"


def max_page(ingredient, start=1):
    pages = []
    response = ingredient_response(ingredient, start)
    soup = BeautifulSoup(response.text, 'html.parser')
    pages_no = soup.find('ul', class_='pagination')
    for page in pages_no:
        pages.append(page.find('a', class_='page-link').string)
    return int(pages[-2])
