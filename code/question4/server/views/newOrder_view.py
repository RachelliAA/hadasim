from PySide6.QtWidgets import QMainWindow, QMessageBox, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QCheckBox, QButtonGroup
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

from PySide6.QtWidgets import QWidget, QVBoxLayout, QListWidget
import sys

class NewOrderView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Item List View")
        self.setFixedSize(800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.layout = QVBoxLayout()
        central_widget.setLayout(self.layout)

        self.add_main_fields()

    def add_main_fields(self):
        title_label = QLabel("Item List", self)
        title_label.setStyleSheet("font-size: 30px;")
        title_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(title_label)

        self.item_list = QListWidget()
        self.layout.addWidget(self.item_list)

    def update_item_list(self, items):
        self.item_list.clear()
        for item in items:
            self.item_list.addItem(f"{item.item_id}: {item.name} - {item.price} (Min: {item.min_amount})")

    def show_information(self, message):
        QMessageBox.information(self, "Information", message)

    def show_warning(self, message):
        QMessageBox.warning(self, "Warning", message)
