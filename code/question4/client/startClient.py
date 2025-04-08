from PySide6.QtWidgets import QApplication

import sys
from views.logIn_view import LoginView
from controllers.login_controller import LoginController

##STARTS FROM LOGIN


def main():
    #create the application
    app = QApplication(sys.argv)

    login_view = LoginView()

    controller = LoginController( login_view)

    login_view.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
    