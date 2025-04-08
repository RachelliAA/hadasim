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
