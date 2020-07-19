from PyQt5.QtWidgets import *


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setGeometry(300, 300, 320, 180)
        self.setWindowTitle("GGL_Player")

        self.show()
