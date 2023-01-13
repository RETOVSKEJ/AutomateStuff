from pytube import Playlist, exceptions, YouTube
import os

def main():
    linkType = input("type p to download playlist or skip to download single link: ")
    desiredPath = "E:\\Muzyka"
    create_path(desiredPath)

    if linkType == 'p' or linkType == 'P':
        print("Wybrales playliste...")
        link = input("Enter the link to the playlist")
        playlist = Playlist(link)
        print(f"Dlugosc playlisty: {playlist.length}")
        print("od ktorej piosenki zaczac? wpisz 1 pobierac od samej gory")
        startFrom = validate_input(playlist.length)
        print("Ile piosenek pobrac?")
        downloadAmount = validate_input(playlist.length)
        downloadPlaylist(downloadAmount, playlist, desiredPath, startFrom)
    else:
        print("wybrales pojedynczy link...")
        link = input("Enter the link to the video")
        yt = YouTube(link)
        print(f"Tytul Piosenki: {yt.title}")
        downloadLink(yt, desiredPath)


def validate_input(value):
    downloadAmount = 0
    while True:
        try:
            downloadAmount = int(input("Enter an integer 1-%i: " % value))
        except ValueError:
            print("Please enter a valid integer 1-%i" % value)
            continue
        if downloadAmount >= 1 and downloadAmount <= value:
            print(f'You entered: {downloadAmount}')
            return downloadAmount
        else:
            print('The integer must be in the range 1-%i' % value)

def create_path(desiredPath):
    if os.path.isdir(desiredPath) == False:
        os.mkdir(desiredPath)
        print("Stworzono folder %s" % desiredPath)
    else:
        print("Folder %s JUZ ISTNIEJE" % desiredPath)


def downloadPlaylist(downloadAmount, playlist, desiredPath, startFrom):
    counter = 0
    if startFrom != 0: 
        startFrom -= 1   # zeby index w tablicy byl od zera
        downloadAmount = downloadAmount + startFrom



    for song in playlist.videos[startFrom:downloadAmount]:
        counter += 1
        songsLeft = downloadAmount - counter
        if os.path.exists(os.path.join(desiredPath, song.title) + ".mp4"):
            print("File %s already exists" % song.title)
        else:
            try:
                mp4 = song.streams.get_by_itag('140')
            except (exceptions.VideoUnavailable, exceptions.VideoPrivate, exceptions.AgeRestrictedError) as err:
                if err == exceptions.VideoUnavailable:
                    print("Video %s is unavaialable, skipping." % song.title)
                if err == exceptions.VideoPrivate:
                    print("Video %s is private, skipping..." % song.title)
                if err == exceptions.AgeRestrictedError:
                    print("Video $s is age restricted, can't download" % song.title)
            else:
                mp4.download(desiredPath)
                print("Succesfully downloaded %s" % song.title)
                print("%i songs left..."  % songsLeft)


def downloadLink(link, desiredPath):
    if os.path.exists(os.path.join(desiredPath, link.title) + ".mp4"):
        print("File %s already exists in given directory" % link.title)
    else:
        try:
            mp4 = link.streams.get_by_itag('140')
        except (exceptions.VideoUnavailable, exceptions.VideoPrivate, exceptions.AgeRestrictedError) as err:
            if err == exceptions.VideoUnavailable:
                print("Video %s is unavaialable, skipping." % link.title)
            if err == exceptions.VideoPrivate:
                print("Video %s is private, skipping..." % link.title)
            if err == exceptions.AgeRestrictedError:
                print("Video $s is age restricted, can't download" % link.title)
        else:
            mp4.download(desiredPath)
            print("Succesfully downloaded %s" % link.title)

if __name__=="__main__":
    main()
