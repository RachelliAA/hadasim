from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox, QWidget, QVBoxLayout, QLabel, QPushButton
from PySide6.QtCore import Qt

from PySide6.QtWidgets import QWidget, QVBoxLayout, QListWidget
import sys

from controllers.main_controller import MainController
#from server.controllers import main_controller
class MainView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main View")
        self.setFixedSize(800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.layout = QVBoxLayout()
        central_widget.setLayout(self.layout)

        self.add_main_fields()

    def add_main_fields(self):
        title_label = QLabel("Hello Grocer", self)
        title_label.setStyleSheet("font-size: 30px;")
        title_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(title_label)

        self.order_list = QListWidget()
        self.layout.addWidget(self.order_list)

        self.deliver_button = QPushButton("Mark as Delivered")
        self.deliver_button.setVisible(False)
        self.layout.addWidget(self.deliver_button)

        self.new_order_button = QPushButton("New Order")
        self.layout.addWidget(self.new_order_button)

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
