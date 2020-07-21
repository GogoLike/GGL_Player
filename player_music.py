import pyglet


class TPSong:

    def __init__(self, song_path):
        self.path = song_path

    def playsound(self):
        song = pyglet.media.load(self.path)
        song.play()

        pyglet.app.run()

    def stopsound(self):
        pyglet.app.exit()
