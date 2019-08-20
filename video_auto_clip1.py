import glob
from moviepy.editor import *
import moviepy.video.fx.resize as video_resize

def clip_video(video_path,n,max_video_size=24,ratio=0.5):
    # video path path of video :
    # max_video_size: size of video ,type int  eg:25
    # n :clip the video with n segment
    video = VideoFileClip(video_path).fx(vfx.resize,ratio)
    end_time=video.end
    clip_time=(end_time)//n
    bitrate=(max_video_size*1024*8)//(clip_time+5)

    if ratio != None:

        video.resize(ratio)
       # video_fram_size = video.size
    for i in range(n):
        if i!=n-1:
           result=video.subclip(i*clip_time,(i+1)*clip_time+5)
        else:
            result = video.subclip(i * clip_time, end_time)

        result=CompositeVideoClip([result])
        # codec = 'libx264',
        # audio_codec = 'aac',
        # temp_audiofile = 'temp-audio.m4a',
        # remove_temp = True

        video_name=(video_path.replace('.mp4','-'+str(i+1)+'.mp4')).replace('video','result')
        #video_name = video_path.replace('video', 'result')
        result.write_videofile(video_name,fps=25,bitrate=str(bitrate-76)+'k',audio_bitrate=str(70)+'k',codec = 'libx264',
                               audio_codec='aac', temp_audiofile = 'temp-audio.m4a', remove_temp = True,threads=8)
        result.close()




clip_video('./video.mp4',n=1)





