import os

basepath = 'files'


audio_file = []
audio_info_file = []



#find the correspond information.txt for the specific .3gp audio file
for f_name in os.listdir(basepath):
    if f_name.endswith('.3gp'):
        audio_file.append(f_name)



for f_name in os.listdir(basepath):
    for i in audio_file:
        name = i.strip(".3gp")
        if f_name.startswith('audio_time_info'):
            name_txt = f_name.strip('audio_time_info')
            name_txt = name_txt.strip('.txt')
            if name_txt == name:  #found the info txt we wnat now open it to read info
                #print(name)
                #print(f_name)
                if os.path.isfile(os.path.join(basepath, f_name)):
                    line_number = 2
                    with open(basepath + '/' + f_name,"r") as f:
                        while line_number > 0:
                            tmp = f.readline()
                            the_string = tmp.split("_")
                            print(the_string)
                            if line_number == 2:
                                long_start = 0

                                year_start = int(the_string[0])
                                month_start = int(the_string[1])
                                day_start = int(the_string[2])
                                hour_start = int(the_string[3])
                                minute_start = int(the_string[4])
                                second_start = int(the_string[5])
                                milisecond_start = int(the_string[6])

                                if(month_start == [1,3,5,7,8,10,12]):
                                    long_start = month_start*31
                                elif(month_start == [4,6,9,11]):
                                    long_start = month_start*30
                                elif(month_start == [2]):
                                    long_start = month_start*28

                                long_start = (((((long_start + day_start)*7 + hour_start)*24 + minute_start)*60 + second_start)*1000 + milisecond_start)
                                #print(long_start)
                                
                                
                            elif line_number == 1:
                                long_end = 0
                                year_end = int(the_string[0])
                                month_end = int(the_string[1])
                                day_end = int(the_string[2])
                                hour_end = int(the_string[3])
                                minute_end = int(the_string[4])
                                second_end = int(the_string[5])
                                milisecond_end = int(the_string[6])
                                
                                if(month_end == [1,3,5,7,8,10,12]):
                                    long_end = month_end*31
                                elif(month_end == [4,6,9,11]):
                                    long_end = month_end*30
                                elif(month_end == [2]):
                                    long_end = month_end*28

                                long_end = (((((long_end + day_end)*7 + hour_end)*24 + minute_end)*60 + second_end)*1000 + milisecond_end)
                                #print(long_end)


                            line_number = line_number - 1 

                            

                            #print(tmp)
print(long_end - long_start)                        

                        
                    
            
                

                









        