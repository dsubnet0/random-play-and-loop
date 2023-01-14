from src.big_audio_file import BigAudioFile

def setup():
    my_baf = BigAudioFile(filename="hello_detroit.mp3")

def test_can_create_bigaudiofile(my_baf):
    assert type(my_baf) is BigAudioFile


def test_get_file_length(my_baf):
    assert my_baf.length == 150