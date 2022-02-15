import os
import time_count as count
from moviepy.editor import *

basepath = 'files'

video_file = count.get_video_file(basepath)
video_time_gap = count.video_time_info_gap(video_file,basepath)
video_time_gap_float = video_time_gap/1000

audio_file = count.get_audio_file(basepath)
# print(afloat)

#(0,afloat could be ignore since the video has to be the raw one)
main_video = VideoFileClip(basepath + "/" + video_file).subclip(0,video_time_gap_float)
all_audio = []  

for the_audio in audio_file:
    start_place = 0
    start_place_float = 0.0
    end_place = 0
    end_place_float = 0.0

    the_audio_time_gap = count.specific_audio_time_info_gap(the_audio,basepath)
    the_duration = the_audio_time_gap/1000

    #obtain [#######1,######2]

    start_end = count.video_minus_audio(video_file,the_audio,basepath)
    if (start_end[0] < 0): # video start earlier than audio
        aaaaa = 1
        # make the audio place on the video at specific start time
    elif (start_end[0] > 0):# video start later than audio
        start_place = start_end[0]
        start_place_float = start_place/1000

    if (start_end[1] < 0):# video end earlier than audio
        #duration use the video duration
        all_audio.append(AudioFileClip(basepath + "/" + the_audio).subclip(start_place_float,video_time_gap_float+start_place_float))

    elif (start_end[1] > 0):# video end later than audio
        end_place = start_end[1]
        end_place_float = end_place/1000
        all_audio.append(AudioFileClip(basepath + "/" + the_audio).subclip(start_place_float,end_place_float))

    





new_video = main_video

new_video.write_videofile(filename="my_test1.mp4",codec='libx264')
