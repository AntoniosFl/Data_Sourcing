import sys
import csv
import requests
from bs4 import BeautifulSoup


def write_csv(ingredient, start=1):
    recipes = parse_mult_pages(ingredient, start)
    with open(f'{ingredient}.csv', 'w') as recipes_file:
        writer = csv.DictWriter(recipes_file, fieldnames=recipes[0].keys())
        writer.writeheader()
        for recipe in recipes:
            writer.writerow(recipe)
