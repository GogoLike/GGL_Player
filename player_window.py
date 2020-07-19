import sys
from PyQt5.QtWidgets import *

def start_window():

    app = QApplication(sys.argv)

    main_window = QWidget()
    main_window.resize(320, 180)
    main_window.move(300, 300)
    main_window.setWindowTitle("GGL_Player")
    main_window.show()

    sys.exit(app.exec_())
