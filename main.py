import sys
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtCore import *
import sqlite3
import mutagen


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

        self.file_btn = QPushButton("File", self)
        self.file_btn.setGeometry(580, 500, 50, 25)
        self.file_btn.clicked.connect(self.get_song_path)

        self.file_list = []

        self.create_window()

    def create_window(self):
        self.setGeometry(300, 300, 960, 540)
        self.setMinimumSize(960, 540)
        self.setWindowTitle("Terapsi")

        self.show()

    def get_song_path(self):
        self.file_list = QFileDialog.getOpenFileNames()[0]
        for file in self.file_list:
            TPDatabase.add_in_main_playlist(main_database, file)

    def play_song(self):
        self.player.play()
        self.play_btn.setEnabled(False)
        self.pause_btn.setEnabled(True)

    def pause_song(self):
        self.player.pause()
        self.play_btn.setEnabled(True)
        self.pause_btn.setEnabled(False)


class TPDatabase:
    def __init__(self):
        self.conn = sqlite3.connect("""Terapsi.db""")
        self.cursor = self.conn.cursor()

    def add_in_main_playlist(self, song_path):
        self.cursor.execute("""SELECT COUNT(*) FROM Main_Playlist;""")
        num = str(int(self.cursor.fetchone()[0]) + 1)

        audio_file = mutagen.File(song_path)

        song_name = str(audio_file.tags.getall('TIT2')[0])
        song_singer = str(audio_file.tags.getall('TPE1')[0])
        song_length = str(audio_file.info.length)

        song_data = num + ", '" + song_name + "', '" + song_singer + "', '" + song_path + "', " + song_length

        self.cursor.execute(
            """INSERT INTO Main_Playlist (num, song_name, song_singer, song_path, song_length) VALUES (""" + song_data + """);""")

        self.conn.commit()


if __name__ == '__main__':
    print("Terapsi is started")

    app = QApplication(sys.argv)

    main_database = TPDatabase()

    main_window = MainWindow()

    sys.exit(app.exec_())
