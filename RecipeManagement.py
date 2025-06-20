from data import save_data_to_csv, load_data_from_csv
import csv
from data import PizzaRecipe
class RecipeManagement:
    def __init__(self):
        self.recipes = []
        self.load_data()

    def add_recipe(self, recipe):
        self.recipes.append(recipe)
        self.save_data()
        print(f"Recipe '{recipe.name}' added.")

    def remove_recipe(self, recipe_name):
        for recipe in self.recipes:
            if recipe.name == recipe_name:
                self.recipes.remove(recipe)
                self.save_data()
                print(f"Recipe '{recipe.name}' removed.")
                return
        print(f"Recipe '{recipe_name}' not found.")

    def update_recipe(self, recipe_name, new_ingredients):
        for recipe in self.recipes:
            if recipe.name == recipe_name:
                recipe.ingredients = new_ingredients
                self.save_data()
                print(f"Recipe '{recipe.name}' updated.")
                return
        print(f"Recipe '{recipe_name}' not found.")

    def get_recipe_by_name(self, name):
     for recipe in self.recipes:
        if recipe.name == name:
            print(f"Recipe Name: {recipe.name}")
            print("Ingredients:")
            for ingredient in recipe.ingredients:
                print(f"- {ingredient.name}: {ingredient.quantity} {ingredient.unit}")
            return
        print(f"Recipe '{name}' not found.")

    def list_recipes(self):
        for recipe in self.recipes:
            print(recipe.name)

    def load_data(self):
        self.recipes = load_data_from_csv(PizzaRecipe, 'pizza_recipes.csv', key_field='name')

    def save_data(self):
        save_data_to_csv(self.recipes, 'pizza_recipes.csv')

class PizzaRecipeRepository:
    def save_recipes(self, recipes, filename):
        with open(filename, 'w', newline='') as file:
            fieldnames = recipes[0].to_dict().keys()
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for item in recipes:
                writer.writerow(item.to_dict())
                
    def load_pizza_recipes(self, filename):
        return load_data_from_csv(PizzaRecipe, filename, key_field='name')