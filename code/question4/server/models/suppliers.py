import json
import os


class suppliers:
    def __init__(self,password, name, phone, person, items=[]):
        self.id = 0
        self.items = items
        self.password = password
        self.name = name
        self.phone = phone
        self.person = person

    def __repr__(self):
        return f"Supplier(id={self.id}, name='{self.name}', phone='{self.phone}', person='{self.person}')"
    
    def to_dict(self):
        return {
            "password": self.password,
            "name": self.name,
            "phone": self.phone,
            "person": self.person,
            "items": self.items,
            "id": self.id
        }

    def add_supplier(self): #gets a supplier that i want to add to the DB
        print(self.__dict__)

        suppliers_DB = "suppliers.json"
        # Convert each supplier to a dictionary
        supplier_dict = self.to_dict()

        suppliers_data = []

        try:
            # Check if the file exists
            if os.path.exists(suppliers_DB):
                # If the file exists but is not empty, load the existing data
                if os.path.getsize(suppliers_DB) > 0:
                    with open(suppliers_DB, "r", encoding="utf-8") as f:
                        suppliers_data = json.load(f)
            else:
                # If the file doesn't exist, create it and initialize as an empty list
                with open(suppliers_DB, "w", encoding="utf-8") as f:
                    json.dump(suppliers_data, f, indent=4)

            if suppliers_data:
                next_id = suppliers_data[-1]["id"] + 1 
            else:
                next_id = 1
            supplier_dict["id"] = next_id

            # Append the new supplier as a dict
            suppliers_data.append(supplier_dict)

            # Write the full list back to the file
            with open(suppliers_DB, "w", encoding="utf-8") as f:
                json.dump(suppliers_data, f, indent=4)

            print(f"Appended supplier {self.name} to {suppliers_DB}") 
            return supplier_dict["name"], supplier_dict["id"], 201
        except Exception as e:
            print(f"Error writing to {suppliers_DB}: {e}")
            return None, None, 500
