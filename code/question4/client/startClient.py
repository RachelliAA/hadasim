from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt


import sys
from views.logIn_view import LoginView
from controllers.login_controller import LoginController

##STARTS FROM LOGIN
import sys


def main():
    #create the application
    app = QApplication(sys.argv)

    login_view = LoginView()
    # main_controller = MainController(login_view)
    controller = LoginController( login_view)

    login_view.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
    