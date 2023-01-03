import imageio
import imageio.v2 as iio
import numpy as np
from scipy.interpolate import CubicSpline

# vid = imageio.get_reader(r'videos\vid.mp4','ffmpeg')
# fps = vid.get_meta_data()['fps']
# height,width = vid.get_meta_data()['size']
# w = iio.get_writer(r'videos\vid_output2.mp4', format='FFMPEG', mode='I', fps=int(fps*2))

class Framerate_upscale:
    """class using some techniques to increase framerate on video, 
        idk what i supposed to write more, so...

    Attributes:
        file_dir (str): directory of mp4 file wich be upscaled
        """

    def __init__(self,file_dir:str) -> None:
        self.file_dir = file_dir
        
        # readed file
        self.vid = imageio.get_reader(file_dir,'ffmpeg')

        # metadata
        self.fps = self.vid.get_meta_data()['fps']
        self.height,self.width = self.vid.get_meta_data()['size']


    def mean_upscaling(self, upscaled_dir:str) -> None:
        """upscaling by making frames between two original
        
        Attributes:
            upscaled_dir (str): direcory of upscaled video, must have: .mp4 at the end
        """

        new_file = iio.get_writer(upscaled_dir, format='FFMPEG', mode='I', fps=int(self.fps*2))

        i = False
        for image in self.vid.iter_data():
            if i:    
                new_file.append_data(old_frame)

                #making 4d matrix to easier mean eah color in every pixel
                frame_between = np.zeros((self.width, self.height, 3, 2), np.uint8)
                frame_between[:, :, :, 0] = image
                frame_between[:, :, :, 1] = old_frame
                frame_between = frame_between.mean(axis=3)
                new_file.append_data(frame_between)
            
            i= True
            old_frame = image

        new_file.append_data(image)
        new_file.close()

    def cubic_interp_upscaling(self, upscaled_dir:str) -> None:
        """upscaling by interpolating every color at each pixel

        Attributes:
            upscaled_dir (str): direcory of upscaled video, must have: .mp4 at the end
        """

        new_file = iio.get_writer(upscaled_dir, format='FFMPEG', mode='I', fps=int(self.fps*2))
        data = self.vid.iter_data()
            #making frames
        more_fps_data = []
        for frame in data:
            more_fps_data.append(frame)
            frame_between = np.zeros((self.width, self.height, 3), np.uint8)
            more_fps_data.append(frame_between)
        del more_fps_data[-1]

        # iterate and interpolate
        for y in range(self.width):
            for x in range(self.height):
                for z in range(3):
                    pixel_frame_color = [data[i][y][x][z] for i in range(len(data))] #take nembers for color in pixel
                    timestamp = [*range(0,len(more_fps_data),2)]
                    f = CubicSpline(timestamp,pixel_frame_color)
                    for i in range(len(more_fps_data)):
                        more_fps_data[i][y][x][z] = f(i)
            # print((y/self.width)*100,'%')


        for frame in more_fps_data:
            new_file.append_data(frame)