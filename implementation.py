from data import save_data_to_csv, load_data_from_csv
from InventoryManagement import InventoryManager
from RecipeManagement import RecipeManagement
from MenuManagement import MenuManagement , PizzaMenuItem



class PizzaStore:
    def __init__(self):
        self.inventory_mgr = InventoryManager()
        self.recipe_mgt = RecipeManagement()
        self.menu_mgt = MenuManagement()

    def show_inventory_menu(self):
        self.inventory_mgr.print_inventory()

    def show_recipe_menu(self):
        self.recipe_mgt.list_recipes()

    def show_menu_item_menu(self):
        self.menu_mgt.list_menu_items()

    def process_inventory_menu(self):
        # Implement logic for processing inventory menu
        pass

    def process_recipe_menu(self):
        # Implement logic for processing recipe menu
        pass

    def process_menu_item_menu(self):
        # Implement logic for processing menu item menu
        pass

    def show_main_menu(self):
        # Implement logic for displaying the main menu
        pass




