import design

from PyQt5 import QtWidgets


class QtApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self) -> None:
        """Init function for App
        """
        
        super().__init__()
        self.setFixedSize(800, 600)
        self.setupUi(self)
        