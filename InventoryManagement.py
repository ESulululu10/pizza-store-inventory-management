from data import Ingredient, save_data_to_csv, load_data_from_csv
import csv
class InventoryManager:
    def __init__(self):
        self.ingredients = {}  # Initialize as an empty dictionary
        self.load_data()

    def add_ingredient(self, ingredient):
        if ingredient.name in self.ingredients:
            # If the ingredient already exists, update the quantity
            print("helllo")
            self.ingredients[ingredient.name].quantity += ingredient.quantity
        else:
            print("hello")
            self.ingredients[ingredient.name] = ingredient
        self.save_data()
    def remove_ingredient(self, ingredient_name, quantity):
        if ingredient_name in self.ingredients:
            current_quantity = float(self.ingredients[ingredient_name].quantity)
            quantity = float(quantity)
            if current_quantity >= quantity:
                self.ingredients[ingredient_name].quantity -= quantity
                self.save_data()
                print(f"Removed {quantity} {self.ingredients[ingredient_name].unit} of {ingredient_name}.")
                if self.ingredients[ingredient_name].quantity == 0:
                    print(f"Alert: {ingredient_name} is now out of stock.")
            else:
                print(f"Insufficient quantity of {ingredient_name}.")
        else:
            print(f"Ingredient {ingredient_name} not found in inventory.")

            
    def use_ingredient(self, recipe):
        # Implement logic for using ingredients based on a recipe
        pass

    def check_reorder_levels(self):
        # Implement logic for checking reorder levels and generating alerts
        pass

    def print_inventory(self):
        for ingredient in self.ingredients.values():
            print(f"{ingredient.name}  {ingredient.quantity} {ingredient.unit}")

    def load_data(self):
        loaded_data = load_data_from_csv(Ingredient, 'ingredients.csv', key_field='name')
        self.ingredients = {ingredient.name: ingredient for ingredient in loaded_data}

    def save_data(self):
        save_data_to_csv(list(self.ingredients.values()), 'ingredients.csv')

class IngredientRepository:
    def save_ingredients(self, ingredients, filename):
        with open(filename, 'w', newline='') as file:
            fieldnames = ingredients[0].to_dict().keys()
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for item in ingredients:
                writer.writerow(item.to_dict())

    def load_ingredients(self, filename):
        return load_data_from_csv(Ingredient, filename, key_field='name')
