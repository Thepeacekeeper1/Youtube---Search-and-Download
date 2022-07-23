from pytube import YouTube
from pytube import Search
import time
a=0
sear= input("Enter the video you want to search")
s=Search(sear)
print(f"Number of videos found = {len(s.results)}")
# print(s.results)

res=s.results
for each in s.results:
    each=str(each)
    each=each.split("=")
    each=each[1]
    each=each.replace(">","")
    vid_tit=YouTube(f"https://www.youtube.com/watch?v={each}")
    vid_tit=vid_tit.title
    print(f"Video {a}found :  {vid_tit}")
    a+=1


number =int(input("Enter the video number you want to play"))
print("Selected video  =", s.results[number])
## Till this ok ##
vid= s.results[number]
vid_string =str(vid)
vid_string=vid_string.split("=")
print(vid_string)
vid_f=vid_string[1]
vid_f=vid_f.replace(">","")
print(vid_f)

yt=YouTube(f"https://www.youtube.com/watch?v={vid_f}")
# print(yt)
yt.title
print(yt.title)
# print(yt.streams)
# for each in yt.streams:
#     print(each)
print(yt.streams.filter(res="720p"))

vid_id =int(input("Enter id"))
stream=yt.streams.get_by_itag(vid_id)
stream.download()
time.sleep(500)
