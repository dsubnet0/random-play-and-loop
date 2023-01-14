import vlc
import time

class BigAudioFile() :

    def __init__(self, filename: str):
        self.filename = filename
        # self.audio = vlc.MediaPlayer(f'file://{self.filename}')
        self.media_player = vlc.MediaPlayer()
        self.media = vlc.Media(self.filename)
        self.media_player.set_media(self.media)
        self.media.parse_with_options(0, 0)
        while (not self.media.is_parsed()):
            print('Parsing...')
            self.media_player.play()
            time.sleep(1)
        
    
    def play(self):
        self.media_player.play()
    
    @property
    def length(self):
        return self.media_player.get_length()

if __name__ == '__main__':
    baf = BigAudioFile('hello_detroit.mp3')
    print(baf)
    print(baf.length)
    # baf.play()
    # time.sleep(1)
    # print(baf.media_player.get_length())
    # print(baf.length)