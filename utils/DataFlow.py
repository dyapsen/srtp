
import numpy as np
import cv2

VID_FORMATS = ['asf', 'avi', 'gif', 'm4v', 'mkv', 'mov', 'mp4', 'mpeg', 'mpg', 'wmv']  # include video suffixes
class ImageCapturer:
    def __init__(self, path=None):
        self.path = path

        if self.path:
            self.frame = 0
            self.video_capturer = cv2.VideoCapture(self.path)
            self.frames = int(self.video_capturer.get(cv2.CAP_PROP_FRAME_COUNT))

        else:
            self.video_capturer = None


    def __iter__(self):
        self.count = 0
        return self

    def __next__(self):


        ret_val, img0 = self.video_capturer.read()
        if ret_val:
            self.count += 1

        img = np.ascontiguousarray(img0)

        return self.path, img, img0, self.video_capturer