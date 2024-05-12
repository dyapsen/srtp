import time

from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QFileDialog,
    QVBoxLayout,
    QMenu,
    QAction,
    QAbstractItemView,
    QGraphicsScene,
    QTableWidgetItem,
    QColorDialog,
    QDesktopWidget
)
from PyQt5.QtCore import Qt, QTimer, QThread, pyqtSignal
from PyQt5.QtGui import QImage, QPixmap, QIcon
from collections import deque
from ui.main_win_ui import Ui_MainWindow
from ui.file_ui import Ui_MainWindow_File
from utils.DataFlow import ImageCapturer
from models.unet import ImageSegmentation
from utils.Track import OpticalProcess
from functools import partial
from editor.edit_mode import Editor
import pyqtgraph as pg
import pyqtgraph.exporters
import numpy as np
import os
import cv2
import yaml
import sys
import datetime
import configparser
import math


class TrackThread(QThread):
    def __init__(self):
        super(TrackThread, self).__init__()
        self.pause = False
        self.count = 1
        self.track = OpticalProcess()
    def run(self):
        try:
            time.sleep(3)
            while True:
                if self.pause == False:
                    time.sleep(2)
                    self.track.process_image(self.count)
                    self.count += 1
        except Exception as e:
            print("Exception occurred:", repr(e))

class SliceThread(QThread):
    send_video = pyqtSignal(np.ndarray)
    send_percent = pyqtSignal(int)
    send_time = pyqtSignal(float)

    def __init__(self, view):
        super(SliceThread, self).__init__()
        self.source = '0'
        self.pause = False
        self.brake = False
        self.count = 0
        self.percent_length = 100
        self.video_length = 10
        self.segmentation = ImageSegmentation('202403.pth')
        self.img1 = None
        self.img2 = None
        self.view = view
        self.cpuplot = pg.PlotWidget()  # 使用PlotWidget代替QGraphicsView
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.cpuplot)
        self.view.setLayout(self.layout)
        self.p1 = self.cpuplot.plot(pen='#000000')
        self.cpuplot.setBackground('#FFFFFF')
        # 设置数据存储队列
        self.X = deque([])
        self.Y = deque([])
        self.track = OpticalProcess()
        self.video_length = 100
        self.video_length_time = 1
        self.video_length_time_now = 1
        self.frame_rate = 1
        self.end = False
        self.mode = 0
        self.mode_switch = False
        self.file_switch = False
        self.replay = False

    def run(self):
        data_flow = ImageCapturer(self.source)
        data_flow = iter(data_flow)
        self.count = 0
        path, img, im0s, self.video_capturer = next(data_flow)
        self.send_video.emit(img)
        while True:
            if self.mode_switch or self.file_switch or self.replay:
                data_flow = ImageCapturer(self.source)
                data_flow = iter(data_flow)
                self.count = 0
                path, img, im0s, self.video_capturer = next(data_flow)
                self.send_video.emit(img)
                self.mode_switch = False
                self.file_switch = False
                self.replay = False
                self.X = deque([])
                self.Y = deque([])
            if self.pause == False and self.end == False:
                path, img, im0s, self.video_capturer = next(data_flow)
                if self.count == 0:
                    self.video_length = self.video_capturer.get(cv2.CAP_PROP_FRAME_COUNT)
                    self.frame_rate = self.video_capturer.get(cv2.CAP_PROP_FPS)
                    # 计算视频的时长（以秒为单位）
                    self.video_length_time = self.video_length / self.frame_rate
                self.count += 1
                #time.sleep(0.2)  # 等待33毫秒
                if self.mode == 2:
                    self.img1 = self.img2
                    self.img2 = self.segmentation.segment_images(img, self.count)
                    if self.count >= 2:
                        self.track.process_image(self.img1, self.img2)
                        self.X.append(self.count)  # 添加当前时间戳到 X 轴数据队列
                        self.Y.append(self.track.distance_sum)  # 添加随机生成的数据到 Y 轴数据队列
                        print(self.track.distance_sum)
                        self.xdata = np.array(self.X)  # 转换 X 轴数据队列为 NumPy 数组
                        self.ydata = np.array(self.Y)  # 转换 Y 轴数据队列为 NumPy 数组
                        self.p1.setData(self.xdata, self.ydata)
                        print(self.count, self.video_length)
                        if self.count == self.video_length - 1:
                            self.end == True
                            ex = pg.exporters.ImageExporter(self.cpuplot.scene())

                            success = ex.export(fileName="test.png")

                            if success:
                                print("保存成功！")
                            else:
                                print("保存失败！")
                            break
                    elif self.count == 1:
                        surf = cv2.xfeatures2d.SURF_create(3000)  # 使用SURF进行检测特征点create()中的参数可调，相当于阈值
                        cv2.imwrite('gray_image.jpg', self.img2)
                        gray_image = cv2.imread('gray_image.jpg', 0)  # 读灰度图片
                        #gray_image = cv2.cvtColor(self.im, cv2.COLOR_BGR2GRAY)

                        kp, res = surf.detectAndCompute(gray_image, None)  # 存储需要跟踪的特征点坐标,res不重要
                        self.track.featureC = cv2.KeyPoint_convert(kp)  # 将KeyPoint格式数据中的xy坐标提取出来。
                        self.track.distance_sum_list = [0] * len(self.track.featureC)

                elif self.mode == 3:
                    time.sleep(0.2)
                self.video_length_time_now = self.count / self.frame_rate
                percent = int(self.count / self.video_length * self.percent_length)
                print(self.video_length_time_now,self.count, percent, self.video_length)
                self.send_time.emit(self.video_length_time_now)
                self.send_percent.emit(percent)
                self.send_video.emit(img)

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.path_show.setWordWrap(True)
        self.m_flag = False
        #self.minButton.clicked.connect(self.showMinimized)
        #self.maxButton.clicked.connect(self.max_or_restore)
        # show Maximized window
        #self.maxButton.animateClick(10)
        #self.closeButton.clicked.connect(self.close)
        self.item_cnt = 0



        self.btn_select.clicked.connect(self.open_file)

        self.btn_play_pause.clicked.connect(self.pause_or_continue)
        self.min_window.clicked.connect(self.showMinimized)
        self.max_window.clicked.connect(self.max_or_restore)
        self.max_window.animateClick(10)
        self.close_window.clicked.connect(self.close)

        self.btn_replay.clicked.connect(self.replay)

        self.btn_line.clicked.connect(partial(self.draw_slot, 'line'))
        self.btn_line.setEnabled(False)
        self.btn_line.setVisible(False)

        self.btn_rect.clicked.connect(partial(self.draw_slot, 'rect'))
        self.btn_rect.setEnabled(False)
        self.btn_rect.setVisible(False)

        self.btn_circle.clicked.connect(partial(self.draw_slot, 'ellipse'))
        self.btn_circle.setEnabled(False)
        self.btn_circle.setVisible(False)

        self.btn_curve.clicked.connect(partial(self.draw_slot, 'curve'))
        self.btn_curve.setEnabled(False)
        self.btn_curve.setVisible(False)

        self.btn_draw_image_save.clicked.connect(self.draw_image_save)
        #self.btn_draw_video_save.clicked.connect(self.draw_video_save)

        self.btn_color.clicked.connect(self.setColor)

        self.stackedWidget.setCurrentIndex(1)  # 初始设置不显示任何页
        self.stackedWidget_2.setCurrentIndex(0)  # 初始设置不显示任何页

                    # 进度条
        #self.durationChanged.connect(self.getDuration)
        #self.positionChanged.connect(self.getPosition)
        #self.sld_duration.sliderMoved.connect(self.updatePosition)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.slice = SliceThread(self.curve_view)
        self.slice.send_video.connect(lambda x: self.show_video(x, self.video_label))
        self.slice.send_percent.connect(lambda x: self.progressBar.setValue(x))
        self.slice.send_time.connect(lambda x: self.time_show(x))

        self.mode_choose.clicked.connect(self.showMenu)

        self.btn_confirm_1.clicked.connect(self.get_input_texts_1)
        self.btn_confirm_2.clicked.connect(self.get_input_texts_2)

        # 创建一个 QGraphicsScene 对象
        self.scene = QGraphicsScene(self)
        # 创建一个 QGraphicsView 对象
        self.video_label.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # # 获取 QGraphicsView 的位置、大小并设置给 QGraphicsScene
        # video_label_pos = self.video_label.mapToGlobal(self.video_label.pos())
        # video_label_rect = self.video_label.geometry()
        # scene_rect = QRectF(video_label_pos.x(), video_label_pos.y(), video_label_rect.width(),
        #                     video_label_rect.height())
        # print(scene_rect)
        # self.scene.setSceneRect(scene_rect)
        # #self.scene.setSceneRect(view_rect)
        # self.scene.setBackgroundBrush(Qt.transparent)
        self.item_cnt = 0
        self.file_route = None
        print(self.video_label.mapToGlobal(self.video_label.pos()))
        self.video_label = Editor(self.video_label)
        self.video_label.main_window = self
        self.video_label.setScene(self.scene)
        self.config = configparser.ConfigParser()
        config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "settings\\file_records.ini")
        self.config.read(config_path, encoding='utf-8')

        self.recall_btn.clicked.connect(self.video_label.drawing_record.undo)
        self.restore_btn.clicked.connect(self.video_label.drawing_record.redo)

        self.nw = 0
        self.nh = 0

        self.img = None

        self.center()

    def replay(self):
        self.slice.replay = True

    def center(self):
        # 获取屏幕的尺寸信息
        screen = QDesktopWidget().screenGeometry()
        # 获取窗口的尺寸信息
        size = self.geometry()
        # 将窗口移动到指定位置
        print(screen)
        print(size)
        print((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)


    def draw_image_save(self):
        # 创建一个和self.img相同大小的黑色画布
        canvas = np.zeros_like(self.img)
        # 遍历所有的画笔操作
        for item in self.video_label.drawing_record.editor_collect:
            # 获取坐标和颜色
            coordinates = item['coordinates']
            color = item['color']

            # 将QColor转换为BGR格式的颜色值
            bgr_color = [color.blue(), color.green(), color.red()]
            print(bgr_color)
            for point in coordinates:
                # 将坐标转换为整数类型
                x = int(point.x)
                y = int(point.y)
                # 在画布上绘制圆形
                radius = 1  # 定义圆形的半径
                thickness = -1  # 定义圆形的填充模式
                cv2.circle(canvas, (x, y), radius, bgr_color, thickness)

        # 将绘制结果与原始图像叠加
        alpha = 0.5  # 定义叠加的透明度
        result = cv2.addWeighted(self.img, 1 - alpha, canvas, alpha, 0)
        save_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "file\\output.png")
        # 将结果保存到指定的路径中
        cv2.imwrite(save_path, result)

    def setColor(self):
        temp_color = QColorDialog.getColor()
        if temp_color.isValid():
            self.video_label.color = temp_color
            self.color_show.setStyleSheet(f'background-color: {temp_color.name()}')


    def set_file_route(self, file_route, file_size):
        self.file_route = file_route
        if self.file_route:
            file_route_text = '文件路径：{}'.format(file_route)
            self.path_show.setText(file_route_text)
            file_size_text = '文件大小：{}'.format(file_size)
            self.size_show.setText(file_size_text)
            self.slice.source = self.file_route
            self.slice.pause = True
            if not self.slice.isRunning() :
                self.slice.start()
                bofang_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "icon\\bofang.svg")
                self.btn_play_pause.setIcon(QIcon(bofang_path))

    def get_id(self, inc=False):
        if inc:
            self.item_cnt += 1
        return str(self.item_cnt)

    def draw_slot(self, type):
        self.video_label.drawing = True
        self.video_label.start(type)

    def showMenu(self):
        menu = QMenu(self)
        actions = []

        action_names = ['edit_mode', 'yingli_mode', 'yingbian_mode', 'bofang_mode']
        for action_name in action_names:
            action = QAction(action_name, self)
            action.triggered.connect(lambda checked, name=action_name: self.mode_switch(name))
            actions.append(action)
            menu.addAction(action)

        button = self.sender()
        menuWidth = menu.sizeHint().width()
        menuHeight = menu.sizeHint().height()
        buttonPos = button.mapToGlobal(button.rect().bottomRight())

        menu.move(buttonPos.x() - menuWidth, buttonPos.y())
        menu.exec_()

    def mode_switch(self, option_name):
        if not self.slice.pause:
            self.btn_play_pause.animateClick(10)

        if option_name == 'edit_mode':
            # 显示隐藏的按钮
            self.slice.mode = 3
            self.slice.mode_switch = True
            self.btn_line.setEnabled(True)
            self.btn_line.setVisible(True)
            self.btn_rect.setEnabled(True)
            self.btn_rect.setVisible(True)
            self.btn_circle.setEnabled(True)
            self.btn_circle.setVisible(True)
            self.btn_curve.setEnabled(True)
            self.btn_curve.setVisible(True)
            self.mode_choose.setText('编辑')
            self.stackedWidget.setCurrentIndex(2)  # 初始设置不显示任何页
            self.stackedWidget_2.setCurrentIndex(2)  # 初始设置不显示任何页

        elif option_name == 'yingli_mode':
            self.slice.mode_switch = True
            self.video_label.drawing = False
            self.btn_line.setEnabled(False)
            self.btn_line.setVisible(False)
            self.btn_rect.setEnabled(False)
            self.btn_rect.setVisible(False)
            self.btn_circle.setEnabled(False)
            self.btn_circle.setVisible(False)
            self.btn_curve.setEnabled(False)
            self.btn_curve.setVisible(False)
            self.slice.mode = 2
            self.slice.track.mode = 0
            self.mode_choose.setText('应力')
            self.stackedWidget.setCurrentIndex(0)  # 初始设置不显示任何页
            self.stackedWidget_2.setCurrentIndex(3)  # 初始设置不显示任何页
            self.slice.cpuplot.setTitle('Stress')
            # 设置横纵坐标轴
            self.slice.cpuplot.setLabel('bottom', text='Time', units='f')  # 设置横轴标签为时间，单位为秒
            self.slice.cpuplot.setLabel('left', text='Stress', units='GPa')  # 设置纵轴标签为压强

        elif option_name == 'bofang_mode':
            self.slice.mode_switch = True
            self.video_label.drawing = False
            self.btn_line.setEnabled(False)
            self.btn_line.setVisible(False)
            self.btn_rect.setEnabled(False)
            self.btn_rect.setVisible(False)
            self.btn_circle.setEnabled(False)
            self.btn_circle.setVisible(False)
            self.btn_curve.setEnabled(False)
            self.btn_curve.setVisible(False)
            self.mode_choose.setText('播放')
            self.slice.mode = 3
            self.stackedWidget.setCurrentIndex(1)  # 初始设置不显示任何页
            self.stackedWidget_2.setCurrentIndex(0)  # 初始设置不显示任何页

        elif option_name == 'yingbian_mode':
            self.slice.mode_switch = True
            self.video_label.drawing = False
            self.btn_line.setEnabled(False)
            self.btn_line.setVisible(False)
            self.btn_rect.setEnabled(False)
            self.btn_rect.setVisible(False)
            self.btn_circle.setEnabled(False)
            self.btn_circle.setVisible(False)
            self.btn_curve.setEnabled(False)
            self.btn_curve.setVisible(False)
            self.mode_choose.setText('应变')
            self.slice.mode = 2
            self.slice.track.mode = 1
            self.stackedWidget.setCurrentIndex(0)  # 初始设置不显示任何页
            self.stackedWidget_2.setCurrentIndex(1)  # 初始设置不显示任何页
            self.slice.cpuplot.setTitle('Strain')
            # 设置横纵坐标轴
            self.slice.cpuplot.setLabel('bottom', text='Time', units='f')  # 设置横轴标签为时间，单位为秒
            self.slice.cpuplot.setLabel('left', text='Strain', units='%')  # 设置纵轴标签为压强


        else:
            # 隐藏按钮
            print(1)

    def get_input_texts_2(self):
        diameter_text = self.diameter_input.text()
        constant_text = self.constant_input.text()
        scale_text = self.scale_input.text()
        scale_text2 = self.scale_input2.text()
        try:
            diameter = float(diameter_text)
        except ValueError:
            diameter = None  # 默认宽度值

        try:
            constant = float(constant_text)
        except ValueError:
            constant = None  # 默认常数值

        try:
            scale = float(scale_text)
        except ValueError:
            scale = None  # 默认常数值

        try:
            scale2 = float(scale_text2)
        except ValueError:
            scale2 = None  # 默认常数值

        self.slice.track.scale = scale / scale2
        self.slice.track.diameter = diameter
        self.slice.track.constant = constant

    def get_input_texts_1(self):
        x_coordinate1 = self.x_coordinate_1.text()
        x_coordinate2 = self.x_coordinate_2.text()
        y_coordinate1 = self.y_coordinate_1.text()
        y_coordinate2 = self.y_coordinate_2.text()
        try:
            x_coordinate1 = int(x_coordinate1)
        except ValueError:
            x_coordinate1 = None  # 默认宽度值

        try:
            x_coordinate2 = int(x_coordinate2)
        except ValueError:
            x_coordinate2 = None  # 默认宽度值

        try:
            y_coordinate1 = int(y_coordinate1)
        except ValueError:
            y_coordinate1 = None  # 默认高度值

        try:
            y_coordinate2 = int(y_coordinate2)
        except ValueError:
            y_coordinate2 = None  # 默认高度值
        feature1 = np.array([[x_coordinate1, y_coordinate1]])
        feature2 = np.array([[x_coordinate2, y_coordinate2]])
        feature1 = feature1.astype(np.float32)
        feature2 = feature2.astype(np.float32)
        self.featureA = np.vstack((feature1, feature2))
        print(self.featureA)
        #
        # self.slice.track.scale = scale / scale2
        # self.slice.track.diameter = diameter
        # self.slice.track.constant = constant

    def max_or_restore(self):
        print(1)
        if self.max_window.isChecked():
            self.showMaximized()
            print(1)
        else:
            self.showNormal()

    def open_file(self):
        open_fold = os.getcwd()
        name, _ = QFileDialog.getOpenFileName(self, 'Video/image', open_fold, "Pic File(*.mp4 *.mkv *.avi *.flv "
                                                                          "*.jpg *.png)")
        # Load file records from an INI file

        file_size = os.path.getsize(name)
        file_size_str = self.convert_size(file_size)

        open_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file_type = os.path.splitext(name)[1].replace(".", "")
        file_section = None
        # 检查是否存在相同文件名的记录
        for section in self.config.sections():
            if self.config[section]['Name'] == name:
                file_section = section
                break

        if file_section is not None:
            # 更新现有记录的打开时间
            self.config[file_section]['OpenTime'] = open_time
        else:
            # 创建新的文件记录
            file_section = f'File{len(self.config.sections()) + 1}'
            self.config[file_section] = {
                'Name': name,
                'Size': file_size_str,
                'OpenTime': open_time,
                'Type': file_type
            }

        record_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "settings\\file_records.ini")
        with open(record_path, 'w',encoding='utf-8') as configfile:
            self.config.write(configfile)
        if name:
            # 设置新的source值
            self.slice.source = name
            # 启动新的线程
            self.slice.file_switch = True
            # if not self.slice.isRunning() :
            #     self.slice.start()
            #     self.btn_play_pause.setIcon(QIcon('./icon/play.svg'))

    def pause_or_continue(self):
        if self.slice.pause == False:
            bofang_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "icon\\bofang.svg")
            self.btn_play_pause.setIcon(QIcon(bofang_path))
            self.slice.pause = True
        else:
            zanting_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "icon\\zanting.svg")
            self.btn_play_pause.setIcon(QIcon(zanting_path))
            self.slice.pause = False

    def mousePressEvent(self, event):
        self.m_Position = event.pos()
        if event.button() == Qt.LeftButton:
            if 0 < self.m_Position.x() < self.frame.pos().x() + self.frame.width() and \
                    0 < self.m_Position.y() < self.frame.pos().y() + self.frame.height():
                self.m_flag = True

    def mouseMoveEvent(self, event):
        if Qt.LeftButton and self.m_flag:
            self.move(event.globalPos() - self.m_Position)

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False

    def show_video(self, img_src, graphics_view):
        self.img = img_src
        try:

            ih, iw, _ = img_src.shape
            w = graphics_view.width()
            h = graphics_view.height()

            # 保持原始宽高比
            if iw / w > ih / h:
                scal = w / iw
                self.nw = w
                self.nh = int(scal * ih)
                img_src_ = cv2.resize(img_src, (self.nw, self.nh))
            else:
                scal = h / ih
                self.nw = int(scal * iw)
                self.nh = h
                img_src_ = cv2.resize(img_src, (self.nw, self.nh))
            print(iw, ih, self.nw, self.nh)
            frame = cv2.cvtColor(img_src_, cv2.COLOR_BGR2RGB)
            img = QImage(frame.data, frame.shape[1], frame.shape[0], frame.shape[1] * frame.shape[2],
                         QImage.Format_RGB888)

            scene = graphics_view.scene()
            pixmap = QPixmap.fromImage(img)
            scene.addPixmap(pixmap)

            graphics_view.setScene(scene)

        except Exception as e:
            print("Error:", e)

    def editor_switch(self):
        # 切换编辑器模式
        self.editor.mode = not self.editor.mode  # 切换编辑器模式的状态

    def time_show(self, x):

        # 假设视频总时长为 12345 秒，当前播放时间为 6789 秒
        total_length = self.slice.video_length_time
        current_time = x


        # 将总时长和当前时间转换为小时、分钟和秒
        total_hours = int(total_length // 3600)
        total_minutes = int((total_length % 3600) // 60)
        total_seconds = int(total_length % 60)

        current_hours = int(current_time // 3600)
        current_minutes = int((current_time % 3600) // 60)
        current_seconds = int(current_time % 60)
        time_format = '{:02d}:{:02d}:{:02d}/{:02d}:{:02d}:{:02d}'.format(current_hours, current_minutes,
                                                                         current_seconds, total_hours, total_minutes,
                                                                         total_seconds)
        time_format2 = '视频总时长: {:02d}:{:02d}:{:02d}'.format(total_hours, total_minutes,
                                                                         total_seconds)

        # 将时间显示在 QLabel 中
        print(total_minutes)
        self.time_show_label.setText(time_format)
        self.duration_show.setText(time_format2)


    def get_id(self, inc=False):
        if inc:
            self.item_cnt += 1
        return str(self.item_cnt)

    @staticmethod
    def convert_size(size_bytes):
        if size_bytes == 0:
            return "0B"
        size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
        i = int(math.floor(math.log(size_bytes, 1024)))
        p = math.pow(1024, i)
        size = round(size_bytes / p, 2)
        return f"{size} {size_name[i]}"

class FileWindow(QMainWindow, Ui_MainWindow_File):
    def __init__(self, parent=None):
        super(FileWindow, self).__init__(parent)
        self.setupUi(self)
        self.m_flag = False
        self.file_table.setColumnCount(4)
        self.file_table.setShowGrid(False)
        self.file_table.verticalHeader().setVisible(False)
        self.file_table.setHorizontalHeaderLabels(["最近文件名", "大小", "上次打开时间", "文件类型"])
        self.file_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.file_table.itemClicked.connect(self.open_recent_file)

        self.min_window.clicked.connect(self.showMinimized)
        self.max_window.clicked.connect(self.max_or_restore)
        self.close_window.clicked.connect(self.close)

        for j in range(3):
            self.file_table.setColumnWidth(j, 200)  # 设置第j列的宽度为100像素
        self.file_table.horizontalHeader().setStretchLastSection(True)
        self.config = configparser.ConfigParser()



        self.btn_select_win1.clicked.connect(self.open_new_file)
        config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "settings\\file_records.ini")
        self.config.read(config_path, encoding='utf-8')
        # 创建一个空列表
        self.file_list = []

        # 遍历配置文件中的节（sections）
        for section in self.config.sections():
            # 创建一个字典，用于存储每个节的数据
            section_data = {}

            # 获取每个节中的键值对
            options = self.config.items(section)

            # 遍历每个键值对，将选项名和对应的值存储到字典中
            for option, value in options:
                section_data[option] = value

            # 将每个节的数据字典添加到列表中
            self.file_list.append(section_data)

        # 打印列表
        for section in self.config.sections():
            self.data = [self.config.get(section, option) for option in self.config.options(section)]
            self.add_row()
        self.center()

    def center(self):
        # 获取屏幕的尺寸信息
        screen = QDesktopWidget().screenGeometry()
        # 获取窗口的尺寸信息
        size = self.geometry()
        # 将窗口移动到指定位置
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)

    def max_or_restore(self):
        print(1)
        if self.max_window.isChecked():
            self.showMaximized()
            print(1)
        else:
            self.showNormal()

    def add_row(self):
        row_position = self.file_table.rowCount()
        self.file_table.insertRow(row_position)

        for i, item in enumerate(self.data):
            if i == 0:  # 第一列
                file_name = os.path.basename(item)  # 提取文件名
                self.file_table.setItem(row_position, i, QTableWidgetItem(file_name))
            else:
                self.file_table.setItem(row_position, i, QTableWidgetItem(item))

    def open_recent_file(self, item):
        self.close()
        file_route = self.file_list[item.row()]['name']
        file_size = self.file_list[item.row()]['size']
        if file_route is not None:
            myWin = MainWindow()
            myWin.set_file_route(file_route, file_size)
            myWin.show()



    def open_new_file(self):
        open_fold = os.getcwd()
        name, _ = QFileDialog.getOpenFileName(self, 'Video/image', open_fold, "Pic File(*.mp4 *.mkv *.avi *.flv "
                                                                          "*.jpg *.png)")
        # Load file records from an INI file


        file_size = os.path.getsize(name)
        file_size_str = self.convert_size(file_size)
        open_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file_type = os.path.splitext(name)[1].replace(".", "")
        file_section = None

        # 检查是否存在相同文件名的记录
        for section in self.config.sections():
            if self.config[section]['Name'] == name:
                file_section = section
                break

        if file_section is not None:
            # 更新现有记录的打开时间
            self.config[file_section]['OpenTime'] = open_time
        else:
            # 创建新的文件记录
            file_section = f'File{len(self.config.sections()) + 1}'
            self.config[file_section] = {
                'Name': name,
                'Size': file_size_str,
                'OpenTime': open_time,
                'Type': file_type
            }
        self.close()
        record_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "settings\\file_records.ini")
        with open(record_path, 'w', encoding='utf-8') as configfile:
            self.config.write(configfile)
        myWin = MainWindow()
        myWin.set_file_route(name, file_size_str)
        myWin.show()

    def mousePressEvent(self, event):
        self.m_Position = event.pos()
        if event.button() == Qt.LeftButton:
            if 0 < self.m_Position.x() < self.frame.pos().x() + self.frame.width() and \
                    0 < self.m_Position.y() < self.frame.pos().y() + self.frame.height():
                self.m_flag = True

    def mouseMoveEvent(self, event):
        if Qt.LeftButton and self.m_flag:
            self.move(event.globalPos() - self.m_Position)

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False

    @staticmethod
    def convert_size(size_bytes):
        if size_bytes == 0:
            return "0B"
        size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
        i = int(math.floor(math.log(size_bytes, 1024)))
        p = math.pow(1024, i)
        size = round(size_bytes / p, 2)
        return f"{size} {size_name[i]}"

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = FileWindow()
    myWin.show()
    # myWin.showMaximized()
    sys.exit(app.exec_())
