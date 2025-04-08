import json
import os


class Item:
    def __init__(self, name, price, min_amount, supplier_id):
        self.item_id = 0
        self.name = name
        self.price = price
        self.min_amount = min_amount
        self.supplier_id = supplier_id

    def __repr__(self):
        return f"Item(id={self.item_id}, name={self.name}, price={self.price}, min_amount={self.min_amount}, supplier_id={self.supplier_id})"

    def to_dict(self):
        return {
            "item_id": self.item_id,
            "name": self.name,
            "price": self.price,
            "min_amount": self.min_amount,
            "supplier_id": self.supplier_id
        }
    
    def from_dict(self, data):
        self.item_id = data.get("item_id", self.item_id)
        self.name = data.get("name", self.name)
        self.price = data.get("price", self.price)
        self.min_amount = data.get("min_amount", self.min_amount)
        self.supplier_id = data.get("supplier_id", self.supplier_id)
        return self
    
    def add_item(self): #gets a supplier that i want to add to the DB
        print(self.__dict__)

        item_DB = "items.json"
        
        item_dict = self.to_dict()

        items_data = []

        try:
            # Check if the file exists
            if os.path.exists(item_DB):
                # If the file exists but is not empty, load the existing data
                if os.path.getsize(item_DB) > 0:
                    with open(item_DB, "r", encoding="utf-8") as f:
                        items_data = json.load(f)
            else:
                # If the file doesn't exist, create it and initialize as an empty list
                with open(item_DB, "w", encoding="utf-8") as f:
                    json.dump(items_data, f, indent=4)

            if items_data:
                next_id = items_data[-1]["item_id"] + 1 
            else:
                next_id = 1
            item_dict["item_id"] = next_id

            # Append the new item as a dict
            items_data.append(item_dict)

            # Write the full list back to the file
            with open(item_DB, "w", encoding="utf-8") as f:
                json.dump(items_data, f, indent=4)
            return item_dict["item_id"], item_dict["name"], 200
        except Exception as e:
            print(f"Error: {e}")
            return None
            
            