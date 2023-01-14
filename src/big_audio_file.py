import vlc
import time

class BigAudioFile() :

    def __init__(self, filename: str):
        self.filename = filename
        self.audio = vlc.MediaPlayer(f'file://{self.filename}')
        self.length = self.audio.get_length()
    
    def play(self):
        self.audio.play()