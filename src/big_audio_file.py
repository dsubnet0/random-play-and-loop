import vlc
import time

class BigAudioFile() :

    def __init__(self, filename: str, start_time: int = 0):
        self.filename = filename
        self.start_time = start_time
        self.media_player = vlc.MediaPlayer()
        self.media = vlc.Media(self.filename)
        self.media.add_option(f'start-time={start_time}')
        self.media_player.set_media(self.media)
        self.media_player.play()
        self.media.parse_with_options(0, 0)
        while (not self.media.is_parsed()):
            print('Parsing...')
            time.sleep(1)
        

    @property
    def length(self):
        return self.media_player.get_length()

    
    def play(self):
        self.media_player.play()


    def set_start_time(self, start_time: int):
       self.start_time = start_time
       self.media = vlc.Media(self.filename)
       self.media.add_option(f'start-time={start_time}') 
       self.media_player.set_media(self.media)
    

    def get_start_time(self):
        return self.start_time
        


if __name__ == '__main__':
    baf = BigAudioFile('hello_detroit.mp3', start_time=45)
    print(baf.length)
    # baf.play()
    # while baf.media_player.is_playing():
    #     print('playing...')
    #     time.sleep(1)
    print(baf.get_start_time())