import pytube
from pytube import Youtube

try:
    video_url ='https://www.youtube.com/watch?v=YXY1FhEWM88'

    youtube = pytube.Youtube(video_url)
    video = youtube.stream.first()
    video.download('C:/Users/amgam/Videos/utubedownload')
    print('Download processing')
except:
    print('Yo u fucked up')