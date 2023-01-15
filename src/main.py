import time
import argparse
from random import randrange

from big_audio_file import BigAudioFile

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--filename')
    args = parser.parse_args()

    my_baf_initial = BigAudioFile(args.filename)
    my_baf = BigAudioFile(args.filename, randrange(0, int(my_baf_initial.length/1000)))
    my_baf.media_player.play()
    time.sleep(1)
    while my_baf.media_player.is_playing():
        print('Still playing...')
        time.sleep(5)