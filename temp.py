from moviepy.editor import VideoFileClip, clips_array, vfx
import numpy as np
import cv2, time
from python_interpolate.main import *
import sys, os

file_paths = sys.argv[1]
f = file_paths

Upscaler = Framerate_upscale(f)
methode = None
while not methode:
    methode = input('\n\t1 - mean upscale\n\t2 - quadruple upscale\n\t3 - cubic interpolation upscaling\n\t... ')
    
    if methode == '1':
        Upscaler.mean_upscaling('upscaled.mp4')
    elif methode == '2':
        Upscaler.mean_quadruple_upscaling('upscaled.mp4')
    elif methode == '3':
        Upscaler.cubic_interp_upscaling('upscaled.mp4')
    else:
        print('\nSelect a valid methode\n')
        methode = None


clip1 = VideoFileClip(f)
clip2 = VideoFileClip('upscaled.mp4')
final_clip = clips_array([[clip1, clip2]])
final_clip.resize(width=480).write_videofile("final.mp4")

print('\nPress "q" to close the window\n')

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

ans = input('\n\tDo you want to save the results?\n\tY/N\t... ')

if ans != 'Y':
    os.remove("final.mp4")
os.remove('upscaled.mp4')
