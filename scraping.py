from bs4 import BeautifulSoup

soup = BeautifulSoup(open("carrot/carrot.html"), "html.parser")

for recipe in soup.find_all('p', class_='recipe-name'):
    print(recipe.text)
