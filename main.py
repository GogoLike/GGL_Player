import sys
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtCore import *
import sqlite3


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.song_url = QUrl("""file:///home/igor/Музыка/The_Pixes_-_Whеrе_Is_Mу_Мind.mp3""")
        self.player = QMediaPlayer()
        self.player.setMedia(QMediaContent(self.song_url))

        self.play_btn = QPushButton("Play", self)
        self.play_btn.setGeometry(420, 500, 50, 25)
        self.play_btn.clicked.connect(self.play_song)

        self.pause_btn = QPushButton("Pause", self)
        self.pause_btn.setGeometry(500, 500, 50, 25)
        self.pause_btn.setEnabled(False)
        self.pause_btn.clicked.connect(self.pause_song)

        self.create_window()

    def create_window(self):
        self.setGeometry(300, 300, 960, 540)
        self.setMinimumSize(960, 540)
        self.setWindowTitle("Terapsi")

        self.show()

    def play_song(self):
        self.player.play()
        self.play_btn.setEnabled(False)
        self.pause_btn.setEnabled(True)

    def pause_song(self):
        self.player.pause()
        self.play_btn.setEnabled(True)
        self.pause_btn.setEnabled(False)


if __name__ == '__main__':
    print("Terapsi is started")

    app = QApplication(sys.argv)
    main_window = MainWindow()

    sys.exit(app.exec_())
