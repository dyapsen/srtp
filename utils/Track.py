# import numpy as np
# import cv2
# import time
# import matplotlib.pyplot as plt
# import yaml
# import matplotlib
# import os
# class OpticalProcess:
#     def __init__(self):
#         self.start_image = None
#         self.src_image = None
#         self.real_src_image = None
#         self.featureC = np.array([[23.39620972, 143.55030212]])
#         self.featureC = self.featureC.astype(np.float32)
#         self.featureD = None
#         self.featureA = np.array([[23.39620972, 143.55030212], [23.39620972, 143.55030212]])
#         self.featureA = self.featureA.astype(np.float32)
#         self.featureB = None
#
#         # 将 featureC 的坐标添加到 featureA 中
#         self.writer = None
#         self.x_pixel = 0
#         self.y_pixel = 0
#         self.x = 0
#         self.y = 0
#         self.diameter = 0
#         self.constant = 0
#         self.scale = 0
#         self.dual_x = []
#         self.dual_y = []
#         self.x_initial = 0
#         self.distance_sum = 0
#         self.image_num = 0
#         self.mode = 0
#         self.dual_initial_distance = 0
#         self.dual_initial_distance_delta = 0
#
#     def process_image(self, img1, img2):
#         img1 = cv2.convertScaleAbs(img1)
#         img2 = cv2.convertScaleAbs(img2)
#         if self.mode == 0:
#             self.featureD, features_found2, err2 = cv2.calcOpticalFlowPyrLK(img1, img2, self.featureC, None,
#                                                                      winSize=(90, 90),
#                                                                      maxLevel=5,
#                                                                      criteria=(
#                                                                      cv2.TermCriteria_MAX_ITER | cv2.TermCriteria_EPS,
#                                                                      30, 0.3))
#             distance = np.linalg.norm(self.featureD[0] - self.featureC[0]) * 2
#             if distance < 7:
#                 self.distance_sum += distance
#             self.featureC = self.featureD
#
#         elif self.mode == 1:
#
#             self.featureB, features_found2, err2 = cv2.calcOpticalFlowPyrLK(img1, img2, self.featureA, None,
#                                                                      winSize=(90, 90),
#                                                                      maxLevel=5,
#                                                                      criteria=(
#                                                                      cv2.TermCriteria_MAX_ITER | cv2.TermCriteria_EPS,
#                                                                      30, 0.3))
#
#             if self.dual_initial_distance == 0:
#                 self.dual_initial_distance = np.linalg.norm(self.featureA[0] - self.featureA[1])
#             self.dual_distance_delta = np.linalg.norm(self.featureB[0] - self.featureB[1]) -self.dual_initial_distance
#             self.distance_sum = self.dual_distance_delta
#             self.featureA = self.featureB
#
import numpy as np
import cv2
import time
import matplotlib.pyplot as plt
import yaml
import math
class OpticalProcess:
    def __init__(self):
        self.real_src_image = None
        self.featureC = np.array([[239.39620972, 143.55030212]])
        self.featureD = np.array([[29.39620972, 167.55030212]])
        self.featureC = self.featureC.astype(np.float32)
        self.featureD = self.featureD.astype(np.float32)
        # 将 featureC 的坐标添加到 featureA 中
        self.featureA = np.vstack((self.featureC, self.featureD))
        self.writer = None
        self.x_pixel = 0
        self.y_pixel = 0
        self.x = 0
        self.y = 0
        self.diameter = 1
        self.constant = 1
        self.scale = 1
        self.dual_x = []
        self.dual_y = []
        self.x_initial = 0
        self.distance_sum_list = []
        self.image_num = 0
        self.mode = 0
        self.total = 0
        self.distance_sum = 0
        self.dual_initial_distance = 0
        self.dual_initial_distance_delta = 0

    def process_image(self, img1, img2):
        img1 = cv2.convertScaleAbs(img1)
        img2 = cv2.convertScaleAbs(img2)
        if self.mode == 0:

            self.featureD, features_found2, err2 = cv2.calcOpticalFlowPyrLK(img1, img2, self.featureC, None,
                                                                     winSize=(90, 90),
                                                                     maxLevel=5,
                                                                     criteria=(
                                                                     cv2.TermCriteria_MAX_ITER | cv2.TermCriteria_EPS,
                                                                     30, 0.3))
            for j in range(0, len(self.featureC)):
                distance = math.sqrt((self.featureC[j][0] - self.featureD[j][0]) ** 2 + (self.featureC[j][1] - self.featureD[j][1]) ** 2)
                if distance < 7:
                    self.distance_sum_list[j] += distance
                self.total += 1
            if self.total == 0:
                self.total += 1
            self.distance_sum = sum(self.distance_sum_list) / self.total
            print(self.constant, self.distance_sum, self.diameter, self.scale, self.distance_sum)
            self.distance_sum = 4 * self.distance_sum * self.constant / (3.14 * self.diameter * self.diameter * self.scale)
            self.total = 0

            self.featureC = self.featureD
        elif self.mode == 1:
            self.featureB, features_found2, err2 = cv2.calcOpticalFlowPyrLK(img1, img2, self.featureA, None,
                                                                     winSize=(90, 90),
                                                                     maxLevel=5,
                                                                     criteria=(
                                                                     cv2.TermCriteria_MAX_ITER | cv2.TermCriteria_EPS,
                                                                     30, 0.3))

            if self.dual_initial_distance == 0:
                self.dual_initial_distance = np.linalg.norm(self.featureA[0] - self.featureA[1])
            self.distance_sum = -(np.linalg.norm(self.featureB[0] - self.featureB[1]) -self.dual_initial_distance)/self.dual_initial_distance
            self.featureA = self.featureB

