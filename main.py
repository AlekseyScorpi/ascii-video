import sys
from PyQt5.QtWidgets import QApplication
from qt_app import QtApp

def main():
    app = QApplication(sys.argv)
    window = QtApp()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()