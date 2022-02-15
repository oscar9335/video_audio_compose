from moviepy.editor import *

#cut off the unneeded
main_video = VideoFileClip("main_video.mp4").subclip(0,4*60+20)   # 0s ~ 260s
#no sound
main_video = main_video.volumex(0)

audio_1 = AudioFileClip("sion_start_2sec.mp3",fps = 44100).subclip(0,4*60+20)
audio_1 = audio_1.volumex(0.5)

audio_2 = AudioFileClip("noel_start_6sec.mp3",fps = 44100).subclip(5)
audio_2 = audio_2.volumex(1)

audio_3 = AudioFileClip("inna_start_6sec.mp3",fps = 44100).subclip(5)
audio_3 = audio_3.volumex(1)

audio_4 = AudioFileClip("ayame_start_6sec.mp3",fps = 44100).subclip(5)
audio_4 = audio_4.volumex(1)

audio_5 = AudioFileClip("keikatori_start_2sec.mp3",fps = 44100).subclip(0)
audio_5 = audio_5.volumex(1)


audio_compose = CompositeAudioClip([audio_1,audio_2])



new_video = main_video.set_audio(audio_compose)


new_video.write_videofile(filename="my_test1.mp4",codec='libx264')



#conclusion we can use this to compose all elements we want into a singal video
#however, if we dont have the time stamp to synchronize all clip it will be catastrophe

#another problem have to be solve
# 1. too many sound, if I record the audio on the stree, how can I extract the voice I want,
# 2. All clips are being compressed during the production