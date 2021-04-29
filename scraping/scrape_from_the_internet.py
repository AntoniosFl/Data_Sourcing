import sys
import csv
import requests
from bs4 import BeautifulSoup

base_url = f"https://recipes.lewagon.com/"


def ingredient_response(ingredient, start=1):
    return requests.get(base_url, params={'search[query]': ingredient, 'page': start})
