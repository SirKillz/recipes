import requests
from RecipeItem import RecipeItem


def api_pull(recipe_key):
    sheets_url = f"https://api.sheety.co/28d41c9e28157106a2c489d2dc97c2ce/meijerRecipes/{recipe_key}"
    response = (requests.get(url=sheets_url)).json()

    recipe_item_list = []
    for item in response[recipe_key]:
        if 'subURL' in response[recipe_key]:
            recipe_item = RecipeItem(name=item['recipeItem'], url=item['url'], sub_url=item['subUrl'])
        else:
            recipe_item = RecipeItem(name=item['recipeItem'], url=item['url'], sub_url='')
        recipe_item_list.append(recipe_item)
    return recipe_item_list
