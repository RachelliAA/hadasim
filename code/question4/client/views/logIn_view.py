from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QCheckBox, QButtonGroup
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

from PySide6.QtWidgets import QWidget, QVBoxLayout

#from client.controllers.login_controller import LoginController


from PySide6.QtWidgets import QApplication
import sys
#from client.controllers.login_controller import LoginController
from controllers.login_controller import LoginController


class LoginView(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login View")
        self.setFixedSize(800, 600)

        # Set up central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.layout = QVBoxLayout()              
        central_widget.setLayout(self.layout)    

        self.add_login_fields()                  

        
    def add_login_fields(self):
        # Add a title or logo on the top
        title_label = QLabel("Hello Supplier", self)
        title_label.setStyleSheet("font-size: 100px;")
        title_label.setAlignment(Qt.AlignCenter)
       # title_label.setFont(QFont("Arial", 200, QFont.Bold))
        self.layout.addWidget(title_label)


        # Add "username" field
        username_label = QLabel("Username", self)
        self.layout.addWidget(username_label)
        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText("Enter your username")
        self.layout.addWidget(self.username_input)

        # Add "password" field
        password_label = QLabel("Password", self)
        self.layout.addWidget(password_label)
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)  # Hide the text as password
        self.password_input.setPlaceholderText("Enter your password")
        self.layout.addWidget(self.password_input)

        # Add login button
        self.login_button = QPushButton("Log in", self)
        self.login_button.setStyleSheet("background-color: #1a1a80; color: black; padding: 10px;")
        self.layout.addWidget(self.login_button)

        # Add the second button, but make it initially invisible
        self.signup_button = QPushButton("Sign up", self)
        self.signup_button.setStyleSheet("background-color: #4caf50; color: black; padding: 10px;")
        self.signup_button.setFixedHeight(40)
        self.signup_button.setVisible(True)  # Initially shown
        self.layout.addWidget(self.signup_button)

    #         self.signup_button.setStyleSheet("background-color: #4caf50; color: black; padding: 10px;")  # Original color

    def show_information(self, message):
        QMessageBox.information(self, "Information", message)

    def show_warning(self, message):
        QMessageBox.warning(self, "Warning", message)

