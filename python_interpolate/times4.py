import imageio
import imageio.v2 as iio
import numpy as np

vid = imageio.get_reader(r'videos\ezgif-3-ecec09a53f.mp4','ffmpeg')
fps = vid.get_meta_data()['fps']
height,width = vid.get_meta_data()['size']
w = iio.get_writer(r'videos\my_videox4.mp4', format='FFMPEG', mode='I', fps=int(fps*4))


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

        frame_between2 = np.zeros((width, height, 3, 2), np.uint8)
        frame_between2[:, :, :, 0] = frame_between
        frame_between2[:, :, :, 1] = image
        frame_between2 = frame_between2.mean(axis=3)
        w.append_data(frame_between2)

        frame_between3 = np.zeros((width, height, 3, 2), np.uint8)
        frame_between3[:, :, :, 0] = frame_between2
        frame_between3[:, :, :, 1] = image
        frame_between3 = frame_between3.mean(axis=3)
        w.append_data(frame_between3)
    
    i= True
    old_frame = image

w.append_data(image)
w.close()
