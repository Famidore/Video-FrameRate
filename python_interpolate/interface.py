import numpy as np
import cv2
import time


def play(originalPath = r'videos\horse12.mp4', upscaledPath = r'videos\horse_x4.mp4'):
    names = [originalPath, upscaledPath]
    window_titles = ['Original', 'Upscaled']

    cap = [cv2.VideoCapture(i) for i in names]

    frames = [None] * len(names)
    gray = [None] * len(names)
    ret = [None] * len(names)

    while True:

        for i,c in enumerate(cap):
            if c is not None:
                ret[i], frames[i] = c.read()


        for i,f in enumerate(frames):
            if ret[i] is True:
                gray[i] = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY)
                cv2.imshow(window_titles[i], gray[i])
            elif not ret[0]:
                cap[0].set(cv2.CAP_PROP_POS_FRAMES, 0)
            elif not ret[1]:
                cap[1].set(cv2.CAP_PROP_POS_FRAMES, 0)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    for c in cap:
        if c is not None:
            c.release()

    cv2.destroyAllWindows()