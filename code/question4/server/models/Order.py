import json
import os


class Order:
    def __init__(self, supplier_id, item, status):
        self.id = 0
        self.supplier_id = supplier_id
        self.item = item
        self.status = status

    #returns the next available idfor an order
    # def get_next_order_id():
    #     orders = serverAPI.read_orders()
    #     if not orders:
    #         return 1
    #     last_id = orders[-1] #max(order["id"] for order in orders)
    #     return last_id + 1

    def to_dict(self):
        return {
            "id": self.id,
            "supplier_id": self.supplier_id,
            "item": self.item,
            "status": self.status
        }

    #@staticmethod
    def from_dict(data):
        return Order(
            id=data["id"],
            supplier_id=data["supplier_id"],
            item=data["item"],
            status=data["status"]
        )

    def add_order(self): #gets a supplier that i want to add to the DB
        print(self.__dict__)

        items_DB = "items.json"
        
        item_dict = self.to_dict() #converts the order to a dictionary

        items_data = []

        try:
            # Check if the file exists
            if os.path.exists(items_DB):
                # If the file exists but is not empty, load the existing data
                if os.path.getsize(items_DB) > 0:
                    with open(items_DB, "r", encoding="utf-8") as f:
                        suppliers_data = json.load(f)
            else:
                # If the file doesn't exist, create it and initialize as an empty list
                with open(items_DB, "w", encoding="utf-8") as f:
                    json.dump(suppliers_data, f, indent=4)

            if suppliers_data:
                next_id = suppliers_data[-1]["id"] + 1 
            else:
                next_id = 1
            order_dict["id"] = next_id

            # Append the new supplier as a dict
            suppliers_data.append(order_dict)

            # Write the full list back to the file
            with open(items_DB, "w", encoding="utf-8") as f:
                json.dump(suppliers_data, f, indent=4)

            print(f"Appended order {self.id} to {items_DB}") 
            return order_dict["item"], 201
        except Exception as e:
            print(f"Error writing to {items_DB}: {e}")
            return None, 500