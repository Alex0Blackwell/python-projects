# from __future__ import unicode_literals
import youtube_dl
import shutil


class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')


def download(songURL, title):

    outtmpl = '/songs/' + title + '.%(ext)s'
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': outtmpl,
        # 'o': '/songs/%(title)s.%(ext)s',
        # 'postprocessors': [{
        #     'key': 'FFmpegExtractAudio',
        #     'preferredcodec': 'mp3',
        #     'preferredquality': '192',
        # }],
        'logger': MyLogger(),
        'progress_hooks': [my_hook],
    }

    # file = open('songList/test.txt', 'w')
    # file.write("testing2")
    # file.close()

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        # ydl.download(['https://www.youtube.com/watch?v=U1AOoHSijIk'])
        info = ydl.extract_info(songURL, download=True)
        return info


download('https://www.youtube.com/watch?v=U1AOoHSijIk', 'Acid Rain')
