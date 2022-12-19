import imageio
import imageio.v2 as iio
import numpy as np
from scipy.interpolate import CubicSpline
from scipy.interpolate import interp1d

def o_kurwa(data,shape): #interpolacja każdego piksela

    #making frames
    more_fps_data = []
    for frame in data:
        more_fps_data.append(frame)
        frame_between = np.zeros((width, height, 3), np.uint8)
        more_fps_data.append(frame_between)
    del more_fps_data[-1]

    # iterate and interpolate
    for y in range(shape[0]):
        for x in range(shape[1]):
            for z in range(3):
                pixel_frame_color = [data[i][y][x][z] for i in range(len(data))] #take nembers for color in pixel
                timestamp = [*range(0,len(more_fps_data),2)]
                f = CubicSpline(timestamp,pixel_frame_color)
                for i in range(len(more_fps_data)):
                    more_fps_data[i][y][x][z] = f(i)
        print((y/shape[0])*100,'%')
    
    return more_fps_data



vid = imageio.get_reader(r'Video-FrameRate\python_interpolate\videos\ezgif-3-ecec09a53f.mp4','ffmpeg')
fps = vid.get_meta_data()['fps']
height,width = vid.get_meta_data()['size']
w = iio.get_writer(r'Video-FrameRate\python_interpolate\videos\my_video.mp4', format='FFMPEG', mode='I', fps=int(fps*2))

for frame in o_kurwa([*vid.iter_data()],(width,height)):
    w.append_data(frame)
