def main(ingredient, start=1):
    ingredient = sys.argv[1]
    if ingredient:
        receipes = []
        for page in range(max_page(ingredient)-start+1):
            print(f'Printing Page No.{int(start + 1)}')
            receipes += parse(ingredient, page)
        write_csv(ingredient, start)
        print(f"Wrote recipes to recipes/{ingredient}.csv")
    else:
        print('Usage: python recipe.py INGREDIENT')
        sys.exit(0)

    return receipes
