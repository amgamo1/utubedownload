from pytube import YouTube
import pytube
from pytube.cli import on_progress

video_url = 'https://www.youtube.com/watch?v=YXY1FhEWM88'
max_res = '1080p'
max_abr = '160kbps'

youtube = YouTube(video_url)
print(youtube.streams)
video = youtube.streams.get_by_itag('399')
audio = youtube.streams.filter(abr = max_abr, progressive=False).first()
video.download('C:/Users/amgam/Videos/utubedownload')
audio.download('C:/Users/amgam/Videos/utubedownload')
print('Download processing')