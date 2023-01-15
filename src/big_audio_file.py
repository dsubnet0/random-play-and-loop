import vlc
import time

class BigAudioFile():

    def __init__(self, filename: str, start_time: int = 0):
        self.filename = filename
        self.start_time = start_time

        self.media_player = vlc.MediaPlayer()
        self.media = vlc.Media(self.filename)
        self.media.add_option(f'start-time={start_time}')
        self.media_player.set_media(self.media)

        self.media_player.play()
        time.sleep(1)
        self.length=self.media_player.get_length()
        self.media_player.stop()


    def get_start_time(self):
        return self.start_time
        


if __name__ == '__main__':
    import random
    baf = BigAudioFile('hello_detroit.mp3', start_time=random.randrange(0,298))
    # baf = BigAudioFile('hello_detroit.mp3', start_time=292)
    print(f'length={baf.length}')
    baf.media_player.play()
    time.sleep(1)
    while baf.media_player.is_playing():
        print('playing...')
        time.sleep(1)
    print(baf.get_start_time())