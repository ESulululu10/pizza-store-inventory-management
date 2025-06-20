from implementation import PizzaStore
from InventoryManagement import InventoryManager 
from RecipeManagement import RecipeManagement 
from MenuManagement import MenuManagement   ,PizzaMenuItem
from data import Ingredient , PizzaRecipe


class PizzaStoreUI:
    def __init__(self, pizza_store):
        self.pizza_store = pizza_store

    def display_main_menu(self):
        print("1. Add Ingredient")
        print("2. Remove Ingredient")
        print("3. Show Inventry")
        print("4. Add Recipe")
        print("5. Update Recipe")
        print("6. show all Recipes")
        print("7. Get recipe by name")
        print("8. Remove recipe by name")
        print("9. Add menu Item")
        print("10. Show Menu")
        print("11. Show Menu By catagory")
        print("12. Remove Menu Item")
        print("13. Update Menu Item")
        print("0. Exit")

    def process_user_input(self, user_input):
        if user_input == "1":
            self.add_ingredient_menu()
        elif user_input == "2":
            quantity = input("Enter Quantity to be removed")
            ing_name = input("Enter the name of the Ingredient to be removed")
            self.pizza_store.inventory_mgr.remove_ingredient(ing_name , quantity)
        elif user_input == "3":
            self.pizza_store.inventory_mgr.print_inventory()
        elif user_input == "4":
            self.add_recipe_menu()
        elif user_input == "5":
            self.update_recipe_items()
        elif user_input == "6":
            self.pizza_store.recipe_mgt.list_recipes()
        elif user_input == "7":
            find_name = input("Get recipe by name: ")
            self.pizza_store.recipe_mgt.get_recipe_by_name(find_name)
        elif user_input == "8":
            remnove_name = input("Enter the name of the Recipe to be removed: ")
            self.pizza_store.recipe_mgt.remove_recipe(remnove_name)
        elif user_input == "9":
            self.add_menu_item_menu()
        elif user_input == "10":
           self.pizza_store.menu_mgt.list_menu_items()
        elif user_input == "11":
           Enter_Catagory = input("Enter the Catagory of the Recipe: ")
           self.pizza_store.menu_mgt.get_menu_items_by_category(Enter_Catagory)
        elif user_input == "12":
           remove_menu = input("Enter the menu to be removed: r")
           self.pizza_store.menu_mgt.remove_menu_item(remove_menu)
        elif user_input == "13":
           self.update_menu_items()
        elif user_input == "0":
            exit()
        else:
            print("Invalid input. Please try again.")

    def add_menu_item_menu(self):
        name = input("Enter menu item name: ")
        description = input("Enter menu item description: ")

        # Get size information
        size_name = input("Enter size name: ")
        

        # Get category information
        category_name = input("Enter category name: ")
        
        price = float(input("Enter menu item price: "))

        # Assuming you want to add ingredients to the recipe
        ingredients = []
        while True:
            ingredient_name = input("Enter ingredient name (or 'done' to finish): ")
            if ingredient_name.lower() == 'done':
                break

            quantity = float(input("Enter quantity: "))
            unit = input("Enter unit: ")

            ingredient = Ingredient(ingredient_name, quantity, unit, 0)
            ingredients.append(ingredient)

        recipe = PizzaRecipe(name, ingredients)

        menu_item = PizzaMenuItem(name, description, size_name, price, category_name, recipe)
        self.pizza_store.menu_mgt.add_menu_item(menu_item)
        print(f"Menu item '{name}' added to the menu.")
   
    def update_menu_items(self):
        name = input("Enter menu item name: ")
        description = input("Enter menu item description: ")

        
        size_name = input("Enter size name: ")
       

         # Set the Size class in MenuManagement
        

         # Get category information
        category_name = input("Enter category name: ")
        

        price = float(input("Enter menu item price: "))

         # Assuming you want to add ingredients to the recipe
        ingredients = []
        while True:
             ingredient_name = input("Enter ingredient name (or 'done' to finish): ")
             if ingredient_name.lower() == 'done':
                 break

             quantity = float(input("Enter quantity: "))
             unit = input("Enter unit: ")

             ingredient = Ingredient(ingredient_name, quantity, unit, 0)
             ingredients.append(ingredient)

        recipe = PizzaRecipe(name, ingredients)

        menu_item = PizzaMenuItem(name, description, size_name, price, category_name, recipe)
        self.pizza_store.menu_mgt.update_menu_item(name , menu_item)


    def add_ingredient_menu(self):
        name = input("Enter ingredient name: ")
        quantity = float(input("Enter quantity: "))
        unit = input("Enter unit: ")
        reorder_level = int(input("Enter reorder level: "))
        ingredient = Ingredient(name, quantity, unit, reorder_level)
        self.pizza_store.inventory_mgr.add_ingredient(ingredient)
        print(f"{name} added to inventory.")
    
    def update_recipe_items(self):
        name = input("Enter recipe name: ")
        ingredients = []
        while True:
            ingredient_name = input("Enter ingredient name (or 'done' to finish): ")
            if ingredient_name.lower() == 'done':
                break

            quantity = float(input("Enter quantity: "))
            unit = input("Enter unit: ")

            ingredient = Ingredient(ingredient_name, quantity, unit, 0)
            ingredients.append(ingredient)

        
        self.pizza_store.recipe_mgt.update_recipe(name , ingredients)
        print(f"Recipe '{name}' updated.")

    def add_recipe_menu(self):
        name = input("Enter recipe name: ")
        ingredients = []
        while True:
            ingredient_name = input("Enter ingredient name (or 'done' to finish): ")
            if ingredient_name.lower() == 'done':
                break

            quantity = float(input("Enter quantity: "))
            unit = input("Enter unit: ")

            ingredient = Ingredient(ingredient_name, quantity, unit, 0)
            ingredients.append(ingredient)

        recipe = PizzaRecipe(name, ingredients)
        self.pizza_store.recipe_mgt.add_recipe(recipe)
        print(f"Recipe '{name}' added.")

# Main Program
def main():
    pizza_store = PizzaStore()
    pizza_store_ui = PizzaStoreUI(pizza_store)
    

    while True:
        pizza_store_ui.display_main_menu()
        user_input = input("Enter your choice: ")
        pizza_store_ui.process_user_input(user_input)

if __name__ == "__main__":
    main()