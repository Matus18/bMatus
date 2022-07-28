from pytube import YouTube

link = str(input("Introduce en Link: "))
yt = YouTube(link)
#GET VIDEO
ys = yt.streams.get_highest_resolution()
#GET AUDIO
ys = yt.streams.get_audio_only()
ys.download()
