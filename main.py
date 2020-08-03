import sys
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtCore import *
import sqlite3
import mutagen


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 960, 540)
        self.setMinimumSize(960, 540)
        self.setWindowTitle("Terapsi")

        self.platform = sys.platform

        try:
            self.present_song_url = main_database.get_url_from_number(1)
        except TypeError:
            self.present_song_url = QUrl()

        self.player = QMediaPlayer()
        self.player.setMedia(QMediaContent(self.present_song_url))

        self.name_label = QLabel()
        self.singer_label = QLabel()
        self.length_label = QLabel()

        self.name_label.setText("Name")
        self.singer_label.setText("Singer")
        self.length_label.setText("Duration")

        self.name_label.setAlignment(Qt.AlignCenter)
        self.singer_label.setAlignment(Qt.AlignCenter)
        self.length_label.setAlignment(Qt.AlignCenter)

        self.singer_label.setFixedWidth(300)
        self.length_label.setFixedWidth(120)

        self.list_widget_1 = QListWidget()
        self.list_widget_2 = QListWidget()
        self.list_widget_3 = QListWidget()

        self.list_widget_2.setFixedWidth(300)
        self.list_widget_3.setFixedWidth(120)

        self.list_widget_1.clicked.connect(self.l_widg_1_conn)
        self.list_widget_2.clicked.connect(self.l_widg_2_conn)
        self.list_widget_3.clicked.connect(self.l_widg_3_conn)

        self.play_btn = QPushButton("Play", self)
        self.play_btn.clicked.connect(self.play_song)

        self.pause_btn = QPushButton("Pause", self)
        self.pause_btn.clicked.connect(self.pause_song)

        self.file_btn = QPushButton("File", self)
        self.file_btn.clicked.connect(self.get_song_path)

        self.stop_btn = QPushButton("Stop", self)
        self.stop_btn.clicked.connect(self.stop_song)

        self.clear_btn = QPushButton("Clear", self)
        self.clear_btn.clicked.connect(self.clear_playlist)

        if TPDatabase.how_many_in_main_playlist(main_database) == 0:
            self.play_btn.setEnabled(False)
            self.pause_btn.setEnabled(False)
            self.stop_btn.setEnabled(False)
        else:
            self.play_btn.setEnabled(True)
            self.pause_btn.setEnabled(False)
            self.stop_btn.setEnabled(False)

        main_hbox_1 = QHBoxLayout()
        main_hbox_1.addWidget(self.name_label)
        main_hbox_1.addWidget(self.singer_label)
        main_hbox_1.addWidget(self.length_label)

        main_hbox_2 = QHBoxLayout()
        main_hbox_2.addWidget(self.list_widget_1)
        main_hbox_2.addWidget(self.list_widget_2)
        main_hbox_2.addWidget(self.list_widget_3)
        main_hbox_2.setSpacing(0)

        main_hbox_3 = QHBoxLayout()
        main_hbox_3.addWidget(self.file_btn)
        main_hbox_3.addStretch()
        main_hbox_3.addWidget(self.play_btn)
        main_hbox_3.addWidget(self.pause_btn)
        main_hbox_3.addWidget(self.stop_btn)
        main_hbox_3.addStretch()
        main_hbox_3.addWidget(self.clear_btn)

        main_vbox = QVBoxLayout()
        main_vbox.addLayout(main_hbox_1)
        main_vbox.addLayout(main_hbox_2)
        main_vbox.addLayout(main_hbox_3)

        self.setLayout(main_vbox)

        self.file_list = TPDatabase.read_main_playlist_path(main_database)
        self.add_in_main_playlist()

        self.show()

    def l_widg_1_conn(self):
        row_num = self.list_widget_1.currentRow()
        self.list_widget_2.setCurrentRow(row_num)
        self.list_widget_3.setCurrentRow(row_num)
        self.play_from_num(row_num)

    def l_widg_2_conn(self):
        row_num = self.list_widget_2.currentRow()
        self.list_widget_1.setCurrentRow(row_num)
        self.list_widget_3.setCurrentRow(row_num)
        self.play_from_num(row_num)

    def l_widg_3_conn(self):
        row_num = self.list_widget_3.currentRow()
        self.list_widget_2.setCurrentRow(row_num)
        self.list_widget_1.setCurrentRow(row_num)
        self.play_from_num(row_num)

    def play_from_num(self, num):
        url = main_database.get_url_from_number(num + 1)
        self.player.setMedia(QMediaContent(url))
        self.play_song()

    def get_song_path(self):
        self.file_list = QFileDialog.getOpenFileNames()[0]
        for file in self.file_list:
            file = file.replace('\\', '/')
            TPDatabase.add_in_main_playlist(main_database, file)
        self.add_in_main_playlist()

    def add_in_main_playlist(self):
        for file in self.file_list:
            audio_file = mutagen.File(file)

            try:
                song_name = str(audio_file.tags.getall('TIT2')[0])
            except IndexError:
                song_name = str(file).split("/")[-1].split(".")[0]
            try:
                song_singer = str(audio_file.tags.getall('TPE1')[0])
            except IndexError:
                song_singer = "Unknown"
            song_length = str(audio_file.info.length)

            self.list_widget_1.addItem(QListWidgetItem(song_name))
            self.list_widget_2.addItem(QListWidgetItem(song_singer))
            self.list_widget_3.addItem(QListWidgetItem(song_length))

    def play_song(self):
        self.player.play()
        self.play_btn.setEnabled(False)
        self.pause_btn.setEnabled(True)
        self.stop_btn.setEnabled(True)

    def pause_song(self):
        self.player.pause()
        self.play_btn.setEnabled(True)
        self.pause_btn.setEnabled(False)
        self.stop_btn.setEnabled(True)

    def stop_song(self):
        self.player.stop()
        self.pause_btn.setEnabled(False)
        self.stop_btn.setEnabled(False)
        self.play_btn.setEnabled(True)

    def clear_playlist(self):
        self.file_list = []

        self.list_widget_1.clear()
        self.list_widget_2.clear()
        self.list_widget_3.clear()

        self.stop_song()

        self.play_btn.setEnabled(False)
        self.pause_btn.setEnabled(False)
        self.stop_btn.setEnabled(False)

        TPDatabase.delete_all_from_main_playlist(main_database)


class TPDatabase:
    def __init__(self):
        self.conn = sqlite3.connect("""Terapsi.db""")
        self.cursor = self.conn.cursor()

    def how_many_in_main_playlist(self):
        self.cursor.execute("""SELECT COUNT(*) FROM Main_Playlist;""")
        count = int(self.cursor.fetchone()[0])
        self.conn.commit()
        return count

    def add_in_main_playlist(self, song_path):
        self.cursor.execute("""SELECT COUNT(*) FROM Main_Playlist;""")
        num = str(int(self.cursor.fetchone()[0]) + 1)

        song_data = num + ", '" + song_path + "'"

        self.cursor.execute(
            """INSERT INTO Main_Playlist (num, song_path) VALUES (""" + song_data + """);""")

        self.conn.commit()

    def read_main_playlist_path(self):
        self.cursor.execute("""SELECT song_path FROM Main_Playlist;""")
        file_list = []
        for path in self.cursor.fetchall():
            file_list.append(path[0])

        self.conn.commit()

        return file_list

    def get_url_from_number(self, number):
        number = str(number)
        self.cursor.execute("""SELECT song_path FROM Main_Playlist WHERE num = """ + number + """;""")
        path = str(self.cursor.fetchone()[0])
        url = QUrl("file:///" + path)

        self.conn.commit()

        return url

    def delete_all_from_main_playlist(self):
        self.cursor.execute("""DELETE FROM Main_Playlist WHERE num""")
        self.conn.commit()


if __name__ == '__main__':
    print("Terapsi is started")

    app = QApplication(sys.argv)

    main_database = TPDatabase()

    main_window = MainWindow()

    sys.exit(app.exec_())
