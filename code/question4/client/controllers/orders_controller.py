import json

import requests


class OrdersController:
    def __init__(self, view, supplier_id, model=None):
        self.model = model
        self.view = view
        self.supplier_id = supplier_id
        self.api_url = "http://localhost:5001"
        self.selected_order_id = None
        self.orders = []  
        self.refresh_order_list(supplier_id)
        self.view.order_list.itemClicked.connect(self.order_selected)
        self.view.newItem_button.clicked.connect(self.newItem_button_pressed)
        self.view.deliver_button.clicked.connect(self.mark_selected_order_inProgress)
        self.view.show_deliver_button(False)

    def refresh_order_list(self, supplier_id):
        try:
            # Use the new API endpoint to get orders by supplier_id
            url = f"{self.api_url}/orders/bySupplier/{supplier_id}"
            print(f"Fetching orders for supplier {supplier_id} from {url}")
            
            # Send GET request to the server to fetch orders for a specific supplier
            response = requests.get(url, verify=False)
            
            # Check if the request was successful
            if response.status_code == 200:
                orders = response.json()  # Parse the response JSON to get the orders
                self.view.update_order_list(orders)
            else:
                self.view.show_warning(f"Failed to fetch orders for supplier {supplier_id}: {response.status_code}")
                print(f"Error: {response.text}")
                
        except requests.exceptions.RequestException as e:
            self.view.show_warning(f"An error occurred while fetching orders: {e}")
            print(f"Exception: {e}")


    def mark_selected_order_inProgress(self):
        if self.selected_order_id:
            for order in self.orders:
                if str(order["id"]) == str(self.selected_order_id):
                    order["status"] = "in Progress"
                    break
            
            # Save the updated orders back to the file
            try:
                response = requests.put(f"{self.api_url}/orders/{self.selected_order_id}/inProgress", verify=False)
                if response.status_code == 200:
                    print("Order marked as in progress successfully")
                else:
                    print(f"Failed to mark order as in progress: {response.status_code}")
                self.refresh_order_list(self.supplier_id)
            except Exception as e:
                self.view.show_warning(f"Failed to save orders: {e}")
                print(f"Exception: {e}")

    def order_selected(self, item):
        text = item.text()
        order_id = text.split(":")[0]
        self.selected_order_id = order_id
        self.view.show_deliver_button(True)
    
    
    def newItem_button_pressed(self):
        
        name=self.view.name_input.text()
        price=self.view.price_input.text()
        minamount=self.view.min_amount_input.text()


        if not name or not price or not minamount:
            self.view.show_warning("Please fill in all fields.")
            return
        try:
            newItem = { 
                "name": name,
                "price": price,
                "minamount": minamount,  
                "supplier_id": self.supplier_id
            }

            print(f"New Item: {newItem}")
            api_url = f"{self.api_url}/items"
            print(f"API URL: {api_url}")
            response = requests.post(api_url, json=newItem, verify=False)
            if response.status_code == 201 or response.status_code == 200:
                self.view.show_information("Item added successfully.")
                self.view.name_input.clear()
                self.view.price_input.clear()
                self.view.min_amount_input.clear()
            else:
                self.view.show_warning(f"Failed to add item: {response.status_code}")
                print(f"Error: {response.text}")
        except requests.exceptions.RequestException as e:
            self.view.show_warning(f"An error occurred while adding the item: {e}")
            print(f"Exception: {e}")

            