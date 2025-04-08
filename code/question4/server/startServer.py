##STARTS FROM LOGIN
import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt

from controllers.main_controller import MainController
from views.main_view import MainView

def main():
    #create the application
    app = QApplication(sys.argv)

    view = MainView()
    
    controller = MainController( view)

    view.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
    