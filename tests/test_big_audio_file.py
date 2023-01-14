from src.big_audio_file import BigAudioFile
import pytest

@pytest.fixture
def baf():
    return BigAudioFile(filename="hello_detroit.mp3")

def test_can_create_bigaudiofile(baf):
    assert type(baf) is BigAudioFile


def test_get_file_length(baf):
    assert baf.length == 298086