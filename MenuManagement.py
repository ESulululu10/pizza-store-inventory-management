import csv
from data import save_menu_items_to_csv, load_menu_items_from_csv
from data import Ingredient, PizzaRecipe

class MenuManagement:

    def __init__(self):
        self.menu_items = {}

    def add_menu_item(self, menu_item):
        self.menu_items[menu_item.name] = menu_item
        self.save_data()

    def remove_menu_item(self, name):
        if name in self.menu_items:
            removed_item = self.menu_items.pop(name)
            print(f"Menu item '{name}' removed.")
            self.save_data()
        else:
            print(f"No menu item found with name '{name}'.")

    def update_menu_item(self, name, new_menu_item):
        if name in self.menu_items:
            # Remove the existing items
            removed_item = self.menu_items.pop(name)
            print(f"Menu item '{name}' removed.")

            # Add the updated item
            self.add_menu_item(new_menu_item)
            print(f"Menu item '{name}' updated.")
        else:
            print(f"No menu item found with name '{name}'. Cannot update.")


    def get_menu_items_by_category(self, category):
        print("Debug: Category Name -", category)
        category_items = [item for item in self.menu_items.values() if item.category and item.category.strip() == category.strip()]

        if category_items:
          print(f"Menu items in category '{category}':")
          for menu_item in category_items:
            print(menu_item.name)
        else:
            print(f"No menu items found in category '{category}'.")




    def list_menu_items(self):
     print("Debug: Inside list_menu_items")
     print("Number of menu items:", len(self.menu_items))
     for menu_item in self.menu_items.values():
        print(menu_item.name)


    def load_data(self):
        self.menu_items = load_menu_items_from_csv(PizzaMenuItem, 'menu_items.csv', key_field='name')

    def save_data(self):
        save_menu_items_to_csv(list(self.menu_items.values()), 'menu_items.csv')


class PizzaMenuItem:
    def __init__(self, name, description, size, price, category, recipe):
        self.name = name
        self.description = description
        self.size = size 
        self.price = price
        self.category = category  
        self.recipe = recipe

    def to_dict(self):
        return {
            'name': self.name,
            'description': self.description,
            'size': self.size,
            'price': self.price,
            'category': self.category,
            'recipe': self.recipe.to_dict()
        }

    @classmethod
    def from_dict(cls, data):
        recipe_data = data.pop('recipe')
        recipe = PizzaRecipe.from_dict(recipe_data)

        return cls(recipe=recipe, **data)

class PizzaMenuRepository:
    def save_menu_items(self, menu_items, filename):
        with open(filename, 'w', newline='') as file:
            fieldnames = menu_items[0].to_dict().keys()
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for item in menu_items:
                writer.writerow(item.to_dict())

    def load_menu_items(self, filename):
        return load_menu_items_from_csv(PizzaMenuItem, filename, key_field='name')
