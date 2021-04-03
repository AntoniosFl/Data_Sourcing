import csv


def write_csv(ingredient, recipes):
    with open(f'{ingredient}.csv', 'w') as recipes_file:
        writer = csv.DictWriter(recipes_file, fieldnames=recipes[0].keys())
        writer.writeheader()
        for recipe in recipes:
            writer.writerow(recipe)
