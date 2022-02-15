import os
import time_count as count



basepath = 'files'

audio_file = count.get_audio_file(basepath)
video_file = count.get_video_file(basepath)

a = count.video_time_info_gap(video_file,basepath)
print(a)

# call get_audio_file() to obtain audio_file array[]
for entry in audio_file:
    a = count.specific_audio_time_info_gap(entry,basepath)
    b = count.video_minus_audio(video_file,entry,basepath)
    print(entry)
    print(a)
    for i in b:
        print(i)
    print()
    

