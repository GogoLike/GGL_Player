from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.create_ui()

    def create_ui(self):
        self.setGeometry(300, 300, 960, 540)
        self.setMinimumSize(960, 540)

        self.setWindowTitle("Terpsi")

        self.show()

