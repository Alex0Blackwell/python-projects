# from __future__ import unicode_literals
import youtube_dl


class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def download(title):

    outtmpl = '~/Music/' + title + '.%(ext)s'
    ydl_opts = {
        'format': 'm4a',
        'outtmpl': outtmpl,
        'logger': MyLogger(),
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.extract_info("ytsearch:"+title, download=True)


def main():

    file = open('songList.txt', 'r')
    counter = len(file.readlines())
    file.close()
    for i in range(counter):
        file = open('songList.txt', 'r')
        line = str(file.readlines()[i])[:-1]
        file.close()

        print(f"Downloading: {line}...")
        download(line)
        print("Download complete.")


main()
