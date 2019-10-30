# from __future__ import unicode_literals
import youtube_dl


class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


# def my_hook(d):
#     if d['status'] == 'finished':
#         print('Done downloading, now converting ...')


def download(songURL, title):

    outtmpl = '~/Music/' + title + '.%(ext)s'
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': outtmpl,
        'logger': MyLogger(),
        # 'progress_hooks': [my_hook],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.extract_info(songURL, download=True)


def main():

    file = open('songList/test.txt', 'r')
    counter = len(file.readlines())
    file.close()
    for i in range(counter):
        file = open('songList/test.txt', 'r')
        line = file.readlines()[i]
        file.close()

        title = line.split()[0]
        URL = line.split()[1]

        print(f"Downloading {title}...")
        download(URL, title)
        print("Download complete.")


main()
# download('https://www.youtube.com/watch?v=U1AOoHSijIk', 'Acid Rain')
