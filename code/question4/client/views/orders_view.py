from PySide6.QtWidgets import QMainWindow, QApplication, QListWidget, QMessageBox, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QCheckBox, QButtonGroup
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

from PySide6.QtWidgets import QWidget, QVBoxLayout

class OrdersView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("orders View")
        self.setFixedSize(800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.layout = QVBoxLayout()
        central_widget.setLayout(self.layout)

        self.add_main_fields()

    def add_main_fields(self):
        title_label = QLabel("Here are your Orders:", self)
        title_label.setStyleSheet("font-size: 30px;")
        title_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(title_label)

        self.order_list = QListWidget()
        self.layout.addWidget(self.order_list)

        # Add "name" field
        name_label = QLabel("name", self)
        self.layout.addWidget(name_label)
        self.name_input = QLineEdit(self)
        self.name_input.setPlaceholderText("Enter items name")
        self.layout.addWidget(self.name_input)

        # Add "price" field
        price_label = QLabel("price", self)
        self.layout.addWidget(price_label)
        self.price_input = QLineEdit(self)
        self.price_input.setPlaceholderText("Enter the price")
        self.layout.addWidget(self.price_input)


        # Add "min_amount" field
        min_amount_label = QLabel("min_amount", self)
        self.layout.addWidget(min_amount_label)
        self.min_amount_input = QLineEdit(self)
        self.min_amount_input.setPlaceholderText("Enter your username")
        self.layout.addWidget(self.min_amount_input)


        self.deliver_button = QPushButton("Mark as in Progress")
        self.deliver_button.setVisible(False)
        self.layout.addWidget(self.deliver_button)

        self.newItem_button = QPushButton("add new Item")
        self.layout.addWidget(self.newItem_button)

    def update_order_list(self, orders):
        self.order_list.clear()
        for order in orders:
            self.order_list.addItem(f"{order['id']}: Supplier {order['supplier_id']} - {order['item']} ({order['status']})")


    def show_deliver_button(self, show=True):
        self.deliver_button.setVisible(show)

    def show_information(self, message):
        QMessageBox.information(self, "Information", message)

    def show_warning(self, message):
        QMessageBox.warning(self, "Warning", message)
