# data.py
import csv
import os

# Inside the Ingredient class in data.py
class Ingredient:
    def __init__(self, name, quantity, unit, reorder_level):
        self.name = name
        self.quantity = quantity
        self.unit = unit
        self.reorder_level = reorder_level

    def to_dict(self):
        return {
            'name': self.name,
            'quantity': self.quantity,
            'unit': self.unit,
            'reorder_level': self.reorder_level
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data.get('name', ''),
            quantity=float(data.get('quantity', 0)),
            unit=data.get('unit', ''),
            reorder_level=int(data.get('reorder_level', 0))
        )

class PizzaRecipe:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def to_dict(self):
        return {
            'name': self.name,
            'ingredients': [ingredient.to_dict() for ingredient in self.ingredients]
        }

    @classmethod
    def from_dict(cls, data):
        ingredients_data = data.pop('ingredients', [])  # Ensure ingredients_data is a list
        ingredients = [Ingredient.from_dict(ingredient_data) for ingredient_data in ingredients_data]
        return cls(name=data['name'], ingredients=ingredients)

    

def save_data_to_csv(data, filename):
    if not data:
        print("No data to save.")
        return

    with open(filename, 'w', newline='') as file:
        fieldnames = data[0].to_dict().keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for item in data:
            writer.writerow(item.to_dict())


def load_data_from_csv(cls, filename, key_field=None):
    if not os.path.exists(filename):
        return []

    data = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if 'ingredients' in row:
                row['ingredients'] = eval(row['ingredients'])
            item = cls.from_dict(row)
            if key_field:
                data.append(item)
            else:
                data.append((getattr(item, key_field), item))
    return data




# data.py

def save_menu_items_to_csv(menu_items, filename):
    if not menu_items:
        print("No data to save.")
        return

    with open(filename, 'w', newline='') as file:
        fieldnames = menu_items[0].to_dict().keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for item in menu_items:
            writer.writerow(item.to_dict())

def load_menu_items_from_csv(cls, filename, key_field=None):
    if not os.path.exists(filename):
        return []

    data = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if 'recipe' in row:
                row['recipe'] = eval(row['recipe'])
            item = cls.from_dict(row)
            if key_field:
                data.append(item)
            else:
                data.append((getattr(item, key_field), item))
    return data
