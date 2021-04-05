import sys
import csv
import requests
from bs4 import BeautifulSoup

base_url = f"https://recipes.lewagon.com/"


def parse_mult_pages(ingredient, start=1):
    receipes = []
    for i in range(max_page(ingredient)):
        receipes += parse(ingredient, start)
    return receipes
