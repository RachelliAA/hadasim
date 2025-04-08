from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QCheckBox, QButtonGroup
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

from PySide6.QtWidgets import QWidget, QVBoxLayout

class signupView(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("sign-up View")
        self.setFixedSize(800, 600)

        # Set up central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.layout = QVBoxLayout()             
        central_widget.setLayout(self.layout)   

        self.add_signup_fields() 


    def add_signup_fields(self):
        # Add a title or logo on the top
        title_label = QLabel("sign up", self)
        title_label.setStyleSheet("font-size: 100px;")
        title_label.setAlignment(Qt.AlignCenter)
        # title_label.setFont(QFont("Arial", 200, QFont.Bold))
        self.layout.addWidget(title_label)

        # Add "name" field
        name_label = QLabel("name", self)
        self.layout.addWidget(name_label)
        self.name_input = QLineEdit(self)
        self.name_input.setPlaceholderText("Enter your name")
        self.layout.addWidget(self.name_input)

        # Add "password" field
        password_label = QLabel("password", self)
        self.layout.addWidget(password_label)
        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("Enter password")
        self.layout.addWidget(self.password_input)

        # Add "phone" field
        phone_label = QLabel("phone", self)
        self.layout.addWidget(phone_label)
        self.phone_input = QLineEdit(self)
        self.phone_input.setPlaceholderText("Enter your phone number")
        self.layout.addWidget(self.phone_input)

        # Add "person" field
        person_label = QLabel("person", self)
        self.layout.addWidget(person_label)
        self.person_input = QLineEdit(self)
        self.person_input.setPlaceholderText("Enter your representative person")
        self.layout.addWidget(self.person_input)

        # Add "items" field
        items_label = QLabel("what do you sell? (seperate by ',')", self)
        self.layout.addWidget(items_label)
        self.items_input = QLineEdit(self)
        self.items_input.setPlaceholderText("Enter your items")
        self.layout.addWidget(self.items_input)

        # Add sign up button
        self.signup_button = QPushButton("sign-up", self)
        self.signup_button.setStyleSheet("background-color: #1a1a80; color: white; padding: 10px;")
        self.layout.addWidget(self.signup_button)

    def show_information(self, message):
        QMessageBox.information(self, "Information", message)

    def show_warning(self, message):
        QMessageBox.warning(self, "Warning", message)
