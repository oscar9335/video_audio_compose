#first, obtain the video time info video_start & video_end
#second, obtain the audio[] time info audio_start[] & audio_end[]
# Then, start = ( video_start - audio_start )
#   if(start < 0){
#       use the start to synchronize the video and audio time
#       video is before the audio then use the normal methon tto append the audio onto video background
#   } 
#   if(start > 0){
#       audio is before video
#       make a audio clip make the audio match the video start time 
#   }
#
# Third, Count the end = (video_end - audio_end[])
#   if(end > 0 ){
#       means that the video is longer than audio so need not to do anything         
#   }
#   if(end < 0){
#       cut offc the rest of the audio clip (doesn't need)  
#   }

