import player_window
import sys
from PyQt5.QtWidgets import *

if __name__ == '__main__':
    print("GGL_Player is started")

    app = QApplication(sys.argv)
    main_window = player_window.MainWindow()

    sys.exit(app.exec_())
