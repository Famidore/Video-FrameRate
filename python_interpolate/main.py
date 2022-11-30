import imageio
import imageio.v2 as iio
import numpy as np

vid = imageio.get_reader(r'Video-FrameRate\python_interpolate\videos\ezgif-3-ecec09a53f.mp4','ffmpeg')
fps = vid.get_meta_data()['fps']
height,width = vid.get_meta_data()['size']
w = iio.get_writer(r'Video-FrameRate\python_interpolate\videos\my_video.mp4', format='FFMPEG', mode='I', fps=int(fps*2))


frames = []
i = False
for image in vid.iter_data():
    if i:    
        w.append_data(old_frame)

        frame_between = np.zeros((width, height, 3, 2), np.uint8)
        frame_between[:, :, :, 0] = image
        frame_between[:, :, :, 1] = old_frame
        frame_between = frame_between.mean(axis=3)
        w.append_data(frame_between)
    
    i= True
    old_frame = image

print(np.shape(image))

w.append_data(image)
w.close()

