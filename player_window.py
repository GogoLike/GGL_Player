from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.player = QMediaPlayer()
        self.create_ui()

    def create_ui(self):
        self.setGeometry(300, 300, 960, 540)
        self.setMinimumSize(960, 540)

        self.setWindowTitle("Terpsi")

        self.play_song()

        self.show()

    def play_song(self):
        self.song_url = QUrl("""file:///home/igor/Музыка/The_Pixes_-_Whеrе_Is_Mу_Мind.mp3""")
        self.player.setMedia(QMediaContent(self.song_url))
        self.player.play()

