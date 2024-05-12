
import numpy as np
import torch
import cv2
import os
import re
from models.model import UNet

class ImageSegmentation:
    def __init__(self, model_file):

        self.model_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), model_file)
        self.net = UNet(n_channels=1, n_classes=1)
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.net.to(device=self.device)
        self.net.load_state_dict(torch.load(self.model_file, map_location=self.device))
    def find_max_number_in_folder(self, folder_path):
        max_number = 0

        # 遍历文件夹中的文件
        for filename in os.listdir(folder_path):
            # 使用正则表达式提取文件名中的数字部分
            match = re.search(r'(\d+)', filename)
            if match:
                number = int(match.group(1))
                # 更新最大值
                if number > max_number:
                    max_number = number

        return max_number

    def segment_images(self, img, count):


        # 测试模式
        self.net.eval()

        # 读取所有图片路径
        # tests_path = glob.glob('./dataset4segmentation/image')

        # 读取图片
        # 转为灰度图
        img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        # 转为batch为1，通道为1，大小为512*512的数组
        img = img.reshape(1, 1, img.shape[0], img.shape[1])
        # 转为tensor
        img_tensor = torch.from_numpy(img)
        # 将tensor拷贝到device中，只用cpu就是拷贝到cpu中，用cuda就是拷贝到cuda中。
        img_tensor = img_tensor.to(device=self.device, dtype=torch.float32)
        # 预测
        pred = self.net(img_tensor)
        # 提取结果
        pred = np.array(pred.data.cpu()[0])[0]
        # print(pred)
        # 处理结果
        pred[pred >= 0.5] = 255
        pred[pred < 0.5] = 0
        # 保存图片
        return pred
