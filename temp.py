from moviepy.editor import VideoFileClip, clips_array, vfx
import numpy as np
import cv2, time
from python_interpolate.main import *
import sys, os

file_paths = sys.argv[1]
f = file_paths


Upscaler = Framerate_upscale(f)
Upscaler.mean_quadruple_upscaling('upscaled.mp4')

clip1 = VideoFileClip(f)
clip2 = VideoFileClip('upscaled.mp4').margin(10)
final_clip = clips_array([[clip1, clip2]])
final_clip.resize(width=480).write_videofile("final.mp4")

cap = cv2.VideoCapture('final.mp4')
while(cap.isOpened()):
    
    ret, frame = cap.read() 
    if ret:
        cv2.imshow("Result", frame)
        time.sleep(1/int(cap.get(cv2.CAP_PROP_FPS)))
    else:
       cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
       continue
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    # print(cap.get(cv2.CAP_PROP_FPS))
    
cap.release()
cv2.destroyAllWindows()

os.remove('upscaled.mp4')
# os.remove("final.mp4")