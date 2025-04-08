import json

from controllers.newOrder_controller import NewOrderController
from models import Item
from views.newOrder_view import NewOrderView

class MainController:
    def __init__(self, view, model=None):
        self.model = model
        self.view = view
        self.selected_order_id = None
        self.orders = []  # Hold loaded orders
        self.refresh_order_list()
        self.view.order_list.itemClicked.connect(self.order_selected)
        self.view.deliver_button.clicked.connect(self.mark_selected_order_delivered)
        self.view.new_order_button.clicked.connect(self.open_new_order_view)
        self.view.show_deliver_button(False)

    def refresh_order_list(self):
        try:
            with open("../orders.json", "r") as file:
                self.orders = json.load(file)
                self.view.update_order_list(self.orders)
        except Exception as e:
            self.view.show_warning(f"Failed to load orders: {e}")

    def mark_selected_order_delivered(self):
        if self.selected_order_id:
            for order in self.orders:
                if str(order["id"]) == str(self.selected_order_id):
                    order["status"] = "delivered"
                    break
            print("order", order)
            # Save the updated orders back to the file
            try:
                print("saving orders to file")
                with open("../orders.json", "w") as file:
                    json.dump(self.orders, file, indent=2)
                self.refresh_order_list()
                self.view.show_deliver_button(False)
                self.view.show_information("Order marked as delivered.")
            except Exception as e:
                self.view.show_warning(f"Failed to save orders: {e}")


    def order_selected(self, item):
        text = item.text()
        order_id = text.split(":")[0]
        self.selected_order_id = order_id
        self.view.show_deliver_button(True)


    def open_new_order_view(self):
        # Create the view
        self.view = NewOrderView()

        # Create the controller and link it to the view
        self.model = Item
        self.controller = NewOrderController(self.view, self.model)

        # Show the main view
        self.view.show()