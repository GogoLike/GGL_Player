import player_window
import player_music
import sys
from PyQt5.QtWidgets import *

if __name__ == '__main__':
    print("GGL_Player is started")

    app = QApplication(sys.argv)
    main_window = player_window.MainWindow()

    song = player_music.TPSong("/home/igor/Музыка/The_Pixes_-_Whеrе_Is_Mу_Мind.mp3")
    song.playsound()

    sys.exit(app.exec_())
