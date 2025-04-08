from controllers.orders_controller import OrdersController
from views.orders_view import OrdersView

import requests

class signupController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.api_url = "http://localhost:5001"
        self.view.signup_button.clicked.connect(self.sign_up)       


    def sign_up(self):
            
            name = self.view.name_input.text()
            password = self.view.password_input.text()
            phone = self.view.phone_input.text()
            person = self.view.person_input.text()
            items = self.view.items_input.text()

            # Check if any field is empty
            if not name or not password or not phone or not person or not items:
                self.view.show_information("All fields are required.")
                return
            items_list = items.split(",")
            new_supplier = self.model(password, name, phone, person, items_list)
            print("supplier", new_supplier)


            url = f"{self.api_url}/suppliers"  
            #new_supplier.to_dict() 

            response = requests.post(url, json=new_supplier.to_dict())

            print("Status code:", response.status_code)
            print("Response:", response.json())



            #name, status = self.model.add_supplier(supplier_data)
            print("supplier", new_supplier)
            print("status", response.status_code)
            if response.status_code == 201 or response.status_code == 200:
                self.view.show_information(f"Supplier {name} added successfully.")


                response_data = response.json()  # This is a list, so we need to access the first element
                supplier_data = response_data[0]  # Access the first dictionary in the list
                
                supplier_id = supplier_data.get("supplier_id") 

                self.show_orders_view(name, supplier_id)
                

            else:
                self.view.show_information(f"Failed to add supplier {name}.")
                return

    def show_orders_view(self, username,supplier_id):
        #self.order = Order()
        self.orders_view = OrdersView(username)
        #self.orders_controller = OrdersController(self.traveler_model, self.traveler_view,traveler_id)
        self.orders_controller = OrdersController(self.orders_view,supplier_id)
        self.orders_view.show()      