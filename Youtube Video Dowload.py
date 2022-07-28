from pytube import YouTube

link = str(input("Introduce en Link: "))
yt = YouTube(link)
ys = yt.streams.get_highest_resolution()
ys.download()
