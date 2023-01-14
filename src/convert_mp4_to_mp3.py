import moviepy.editor as mp

if __name__ == '__main__':
    video_clip = mp.VideoFileClip('../Vangelis The Tegos Tapes (1998).mp4')
    video_clip.audio.write_audiofile('vangelis_tegos_tapes.mp3')