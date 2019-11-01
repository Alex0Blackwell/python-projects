import youtube_dl


class MyLogger(object):
    # For debugging and error throwing
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def download(title):
    # Downloads a m4a audio file with the provided title
    outtmpl = '~/Music/' + title + '.%(ext)s'
    ydl_opts = {
        'format': 'm4a',
        'outtmpl': outtmpl,
        'logger': MyLogger(),
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        # Get the top result off youtube
        ydl.extract_info("ytsearch:"+title+"lyrics", download=True)


def main():
    # File minipulation
    file = open('songList.txt', 'r')
    counter = len(file.readlines())
    file.close()

    if(counter != 1):
        file = open('songList.txt', 'w')
        file.write("Enter the names of songs below you wish to download:")
        file.close()
        file = open('songList.txt', 'r+')
        file.truncate(0)
        file.close()
    print("The file \"songList.txt\" had no content. The fle has now been intialized")

    for i in range(1, counter):
        file = open('songList.txt', 'r')
        line = str(file.readlines()[i])[:-1]
        file.close()

        print(f"Downloading: {line}...")
        download(line)
        print("Download complete.")
    print(f"Finished all downloads ({i})")

    # Erases contents of file so no need to re-download songs
    file = open('songList.txt', 'r+')
    file.truncate(0)
    file.close()

    # file = open('songList.txt', 'w')
    # file.write("Enter the names of songs below you wish to download:")
    # file.close()


main()
