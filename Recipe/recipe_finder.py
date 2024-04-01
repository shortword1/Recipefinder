# recipe_finder.py
import requests

def find_recipes(ingredients):
    api_key = "83a44097013a4235afc737dd092f40e4"
    url = "https://api.spoonacular.com/recipes/findByIngredients"
    params = {
        "apiKey": api_key,
        "ingredients": ingredients,
        "number": 5
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        recipes = response.json()
        for recipe in recipes:
            print(f"Recipe: {recipe['title']}\nLink: https://spoonacular.com/recipes/{recipe['title'].replace(' ', '-').lower()}-{recipe['id']}\n")
    else:
        print("Failed to fetch recipes. Please check your API key and internet connection.")

if __name__ == "__main__":
    ingredients = input("Enter ingredients separated by a comma (e.g., apples, flour, sugar): ")
    find_recipes(ingredients)
