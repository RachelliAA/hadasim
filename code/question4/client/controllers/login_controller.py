import requests
from views.orders_view import OrdersView
from controllers.orders_controller import OrdersController
import sys

from controllers.signup_controller import signupController
from views.signup_view import signupView
from models.suppliers import suppliers

class LoginController:
    def __init__(self,  view , model= None):
        self.model = model
        self.view = view
        self.api_url = "http://localhost:5001"
        self.view.login_button.clicked.connect(self.login_button_pressed)
        self.view.signup_button.clicked.connect(self.signup_button_pressed)
        
    def signup_button_pressed(self):

        self.suppliers_model = suppliers
        self.signup_view = signupView()
        self.signup_controller = signupController(self.suppliers_model, self.signup_view)
        self.signup_view.show()
    


    def login_button_pressed(self):
        # Get login data from the view
        username = self.view.username_input.text()
        password = self.view.password_input.text()
        if username and  password:#if not empty
            supplier_id, login_status = self.verify_login(username, password)
            if login_status == 200:
                print("Login successful for supplier id:", supplier_id)
                self.show_orders_view(username,  supplier_id)
            else:
                print("Login Failed")
        else:
            self.view.show_information("Must put in username and password")

    def show_orders_view(self, username,supplier_id):
        
        self.orders_view = OrdersView()
        self.orders_controller = OrdersController(self.orders_view,supplier_id)
        self.orders_view.show()


    def verify_login(self, username, password):
       # return True #for testing so i dont need to log in everytime it works
        # """
        # Generalized login verification for both traveler and admin.
        # """
        login_data = {
            "username": username,
            "password": password
        }
        print(f"attempting login for ", login_data)
        url = f"{self.api_url}/suppliers/login"
        print(url)
        try:
            #return 0, 200
            # Send POST request to the server with login data
            response = response = requests.post(url, json=login_data, verify=False)

            print("login response", response.text)
            # Check if the request was successful
            if response.status_code == 200: #status_code is from the request library. ststus is what i decided
                print("login successful")
                supplier_id = response.json().get("supplier_id")
                return supplier_id, response.status_code
            else:
                print("login failed. Server responded with:", response.status)
                print(f"Error: {response.text}")
                self.view.show_information(f"Error: {response.text}")
                return 0, response.status_code

        except requests.exceptions.RequestException as e:
            self.view.show_information(f"An error occurred: {e}")
            return False