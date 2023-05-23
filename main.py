from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.fx.all import crop
start_time = 5196
end_time = 5230
video_path = "Zindagi Na Milegi Dobara 2011 1080p Bluray 10bit x265 5.1 AAC HEVC Natty-PremiumRelease.mkv"
video = VideoFileClip(video_path)
trimmed_video = video.subclip(start_time, end_time)
trimmed_video.write_videofile("znmd interval scene.mp4")  
