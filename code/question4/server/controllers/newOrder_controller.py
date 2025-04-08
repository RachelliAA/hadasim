# class NewOrderController:
#     def __init__(self, view, model):
#         self.view = view
#         self.items = []  # This will store the list of items.
#         self.model = model

#     def load_items(self):
#         # This is where you would normally fetch items from a database or API.
#         # For now, we can add some mock items:
#         self.items = [
#             self.model(1, "Item 1", 100.0, 10, 1),
#             self.model(2, "Item 2", 150.0, 5, 2),
#             self.model(3, "Item 3", 200.0, 20, 1),
#         ]
#         self.view.update_item_list(self.items)

#     def add_item(self, name, price, min_amount, supplier_id):
#         # Generate a new item and add to the list
#         new_id = len(self.items) + 1  # Generate a new item ID
#         new_item = self.model(new_id, name, price, min_amount, supplier_id)
#         self.items.append(new_item)
#         self.view.update_item_list(self.items)
        
#     def update_item(self, item_id, name=None, price=None, min_amount=None, supplier_id=None):
#         # Update the specified item based on its ID
#         for item in self.items:
#             if item.item_id == item_id:
#                 item.name = name or item.name
#                 item.price = price or item.price
#                 item.min_amount = min_amount or item.min_amount
#                 item.supplier_id = supplier_id or item.supplier_id
#                 self.view.update_item_list(self.items)
#                 return



import json
import os

ITEMS_FILE = "items.json"

class NewOrderController:
    def __init__(self, view, model):
        self.view = view
        self.items = []
        self.model = model

    def load_items(self):
        if not os.path.exists(ITEMS_FILE):
            self.view.show_warning("Items file not found.")
            return

        try:
            with open(ITEMS_FILE, "r") as f:
                data = json.load(f)
                self.items = [
                    self.model(
                        item.get("item_id"),
                        item.get("name"),
                        float(item.get("price")),
                        int(item.get("minamount")),
                        int(item.get("supplier_id"))
                    )
                    for item in data
                ]
            self.view.update_item_list(self.items)
        except Exception as e:
            self.view.show_warning(f"Error loading items: {e}")
