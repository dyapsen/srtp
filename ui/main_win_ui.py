# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_win.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from icon import icon_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1307, 642)
        MainWindow.setStyleSheet("border-radius:4px;\n"
"")
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1161, 591))
        self.frame.setStyleSheet("border-radius: 5px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_1 = QtWidgets.QFrame(self.frame)
        self.frame_1.setGeometry(QtCore.QRect(0, 0, 291, 591))
        self.frame_1.setStyleSheet("QFrame#frame_1{\n"
"    background-color: rgb(123, 169, 255);\n"
"    border-top-left-radius:32px;\n"
"    border-top-right-radius:0px;\n"
"    border-bottom-right-radius:0px;\n"
"    border-bottom-left-radius:32px;\n"
"}")
        self.frame_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_1.setObjectName("frame_1")
        self.inter_tilte = QtWidgets.QPushButton(self.frame_1)
        self.inter_tilte.setGeometry(QtCore.QRect(0, 10, 291, 71))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.inter_tilte.setFont(font)
        self.inter_tilte.setStyleSheet("border:none;\n"
"color: rgb(255, 255, 255);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/svg/namicailiao.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.inter_tilte.setIcon(icon)
        self.inter_tilte.setIconSize(QtCore.QSize(28, 28))
        self.inter_tilte.setObjectName("inter_tilte")
        self.path_show = QtWidgets.QLabel(self.frame_1)
        self.path_show.setGeometry(QtCore.QRect(10, 170, 261, 71))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.path_show.setFont(font)
        self.path_show.setStyleSheet("color: white;")
        self.path_show.setText("")
        self.path_show.setObjectName("path_show")
        self.size_show = QtWidgets.QLabel(self.frame_1)
        self.size_show.setGeometry(QtCore.QRect(10, 260, 271, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.size_show.setFont(font)
        self.size_show.setStyleSheet("color: white;")
        self.size_show.setText("")
        self.size_show.setObjectName("size_show")
        self.duration_show = QtWidgets.QLabel(self.frame_1)
        self.duration_show.setGeometry(QtCore.QRect(10, 310, 191, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.duration_show.setFont(font)
        self.duration_show.setStyleSheet("color: white;")
        self.duration_show.setText("")
        self.duration_show.setObjectName("duration_show")
        self.label_7 = QtWidgets.QLabel(self.frame_1)
        self.label_7.setGeometry(QtCore.QRect(0, 80, 291, 3))
        self.label_7.setStyleSheet("background-color: rgb(247, 247, 247);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame_1)
        self.label_8.setGeometry(QtCore.QRect(0, 80, 291, 71))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("border-top: 1px solid white; \n"
"border-bottom: 1px solid white;\n"
"border-radius: 0;\n"
"color: rgb(242, 251, 255);")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(280, 0, 951, 591))
        self.frame_5.setStyleSheet("")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.frame_4 = QtWidgets.QFrame(self.frame_5)
        self.frame_4.setGeometry(QtCore.QRect(0, 0, 951, 41))
        self.frame_4.setStyleSheet("background-color: #f7f8ff;\n"
"border-top-right-radius:32px;\n"
"border-top-left-radius:0px;\n"
"border-bottom-right-radius:0px;\n"
"border-bottom-left-radius:0px;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.min_window = QtWidgets.QPushButton(self.frame_4)
        self.min_window.setGeometry(QtCore.QRect(830, 0, 41, 41))
        self.min_window.setStyleSheet("QPushButton{\n"
"    border-top-left-radius:0px;\n"
"    border-top-right-radius:0px;\n"
"    border-bottom-right-radius:0px;\n"
"    border-bottom-left-radius:0px;\n"
"    color:#928ae1;\n"
"    icon:url(:/svg/zuixiaohua_purple.svg);\n"
"}    \n"
"\n"
"QPushButton:hover{\n"
"    background-color:rgb(146, 138, 255);\n"
"    border:none;\n"
"    padding: 3px;\n"
"    color: #FFFFFF;\n"
"    icon:url(:/svg/zuixiaohua_white.svg);\n"
"}\n"
"")
        self.min_window.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/svg/minwin.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.min_window.setIcon(icon1)
        self.min_window.setIconSize(QtCore.QSize(26, 26))
        self.min_window.setObjectName("min_window")
        self.max_window = QtWidgets.QPushButton(self.frame_4)
        self.max_window.setGeometry(QtCore.QRect(870, 0, 41, 41))
        self.max_window.setStyleSheet("QPushButton{\n"
"    border-top-left-radius:0px;\n"
"    border-top-right-radius:0px;\n"
"    border-bottom-right-radius:0px;\n"
"    border-bottom-left-radius:0px;\n"
"    color:#928ae1;\n"
"    icon:url(:/svg/zuidahua_purple.svg);\n"
"}    \n"
"\n"
"QPushButton:hover{\n"
"    background-color:rgb(146, 138, 255);\n"
"    border:none;\n"
"    padding: 3px;\n"
"    color: #FFFFFF;\n"
"    icon:url(:/svg/zuidahua_white.svg);\n"
"}\n"
"")
        self.max_window.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/svg/maxwin.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.max_window.setIcon(icon2)
        self.max_window.setIconSize(QtCore.QSize(26, 26))
        self.max_window.setObjectName("max_window")
        self.close_window = QtWidgets.QPushButton(self.frame_4)
        self.close_window.setGeometry(QtCore.QRect(910, 0, 41, 41))
        self.close_window.setStyleSheet("QPushButton{\n"
"    border-top-left-radius:0px;\n"
"    border-top-right-radius:32px;\n"
"    border-bottom-right-radius:0px;\n"
"    border-bottom-left-radius:0px;\n"
"    color:#928ae1;\n"
"    icon:url(:/svg/guanbi_purple.svg);\n"
"}    \n"
"\n"
"QPushButton:hover{\n"
"    border-top-left-radius:0px;\n"
"    border-top-right-radius:32px;\n"
"    border-bottom-right-radius:0px;\n"
"    border-bottom-left-radius:0px;\n"
"    background-color:rgb(146, 138, 255);\n"
"    border:none;\n"
"    padding: 3px;\n"
"    color: #FFFFFF;\n"
"    icon:url(:/svg/guanbi_white.svg);\n"
"}\n"
"")
        self.close_window.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/svg/close.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close_window.setIcon(icon3)
        self.close_window.setIconSize(QtCore.QSize(24, 24))
        self.close_window.setObjectName("close_window")
        self.btn_play_pause = QtWidgets.QPushButton(self.frame_4)
        self.btn_play_pause.setGeometry(QtCore.QRect(810, 10, 21, 21))
        self.btn_play_pause.setStyleSheet("border:none;")
        self.btn_play_pause.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/svg/zanting.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_play_pause.setIcon(icon4)
        self.btn_play_pause.setIconSize(QtCore.QSize(20, 20))
        self.btn_play_pause.setObjectName("btn_play_pause")
        self.progressBar = QtWidgets.QProgressBar(self.frame_4)
        self.progressBar.setGeometry(QtCore.QRect(600, 10, 201, 23))
        self.progressBar.setStyleSheet("QProgressBar{height:22px; text-align:center; font-size:14px; color:rgb(108, 108, 108); border-radius:11px; background:#e7e8f0;}\n"
"QProgressBar::chunk{border-radius:11px;background:qlineargradient(spread:pad,x1:0,y1:0,x2:1,y2:0,stop:0 #99ffff,stop:1 #9900ff);}\n"
"")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.btn_rect = QtWidgets.QPushButton(self.frame_4)
        self.btn_rect.setGeometry(QtCore.QRect(350, 0, 71, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_rect.setFont(font)
        self.btn_rect.setStyleSheet("QPushButton{\n"
"    border-top-left-radius:0px;\n"
"    border-top-right-radius:0px;\n"
"    border-bottom-right-radius:0px;\n"
"    border-bottom-left-radius:0px;\n"
"    color:#928ae1;\n"
"    icon:url(:/svg/rect_purple.svg);\n"
"}    \n"
"\n"
"QPushButton:hover{\n"
"    background-color:rgb(146, 138, 255);\n"
"    border:none;\n"
"    padding: 3px;\n"
"    color: #FFFFFF;\n"
"    icon:url(:/svg/rect_white.svg);\n"
"}\n"
"")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/svg/rect.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_rect.setIcon(icon5)
        self.btn_rect.setIconSize(QtCore.QSize(20, 20))
        self.btn_rect.setObjectName("btn_rect")
        self.btn_circle = QtWidgets.QPushButton(self.frame_4)
        self.btn_circle.setGeometry(QtCore.QRect(280, 0, 71, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_circle.setFont(font)
        self.btn_circle.setStyleSheet("QPushButton{\n"
"    border-top-left-radius:0px;\n"
"    border-top-right-radius:0px;\n"
"    border-bottom-right-radius:0px;\n"
"    border-bottom-left-radius:0px;\n"
"    color:#928ae1;\n"
"    icon:url(:/svg/ellipse_purple.svg);\n"
"}    \n"
"\n"
"QPushButton:hover{\n"
"    background-color:rgb(146, 138, 255);\n"
"    border:none;\n"
"    padding: 3px;\n"
"    color: #FFFFFF;\n"
"    icon:url(:/svg/ellipse_white.svg);\n"
"}\n"
"")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/svg/circle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_circle.setIcon(icon6)
        self.btn_circle.setIconSize(QtCore.QSize(20, 20))
        self.btn_circle.setObjectName("btn_circle")
        self.btn_curve = QtWidgets.QPushButton(self.frame_4)
        self.btn_curve.setGeometry(QtCore.QRect(210, 0, 71, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_curve.setFont(font)
        self.btn_curve.setStyleSheet("QPushButton{\n"
"    border-top-left-radius:0px;\n"
"    border-top-right-radius:0px;\n"
"    border-bottom-right-radius:0px;\n"
"    border-bottom-left-radius:0px;\n"
"    color:#928ae1;\n"
"    icon:url(:/svg/quxian_purple.svg);\n"
"}    \n"
"\n"
"QPushButton:hover{\n"
"    background-color:rgb(146, 138, 255);\n"
"    border:none;\n"
"    padding: 3px;\n"
"    color: #FFFFFF;\n"
"    icon:url(:/svg/quxian_white.svg);\n"
"}\n"
"")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/svg/text.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_curve.setIcon(icon7)
        self.btn_curve.setIconSize(QtCore.QSize(20, 20))
        self.btn_curve.setObjectName("btn_curve")
        self.btn_select = QtWidgets.QPushButton(self.frame_4)
        self.btn_select.setGeometry(QtCore.QRect(0, 0, 71, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_select.setFont(font)
        self.btn_select.setStyleSheet("QPushButton{\n"
"    border-top-left-radius:0px;\n"
"    border-top-right-radius:0px;\n"
"    border-bottom-right-radius:0px;\n"
"    border-bottom-left-radius:0px;\n"
"    color:#928ae1;\n"
"    icon:url(:/svg/wenjian-purple.svg);\n"
"}    \n"
"\n"
"QPushButton:hover{\n"
"    background-color:rgb(146, 138, 255);\n"
"    border:none;\n"
"    padding: 3px;\n"
"    color: #FFFFFF;\n"
"    icon:url(:/svg/wenjian-white.svg);\n"
"}\n"
"")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/svg/folderOpen.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_select.setIcon(icon8)
        self.btn_select.setIconSize(QtCore.QSize(20, 20))
        self.btn_select.setObjectName("btn_select")
        self.mode_choose = QtWidgets.QPushButton(self.frame_4)
        self.mode_choose.setGeometry(QtCore.QRect(70, 0, 71, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.mode_choose.setFont(font)
        self.mode_choose.setStyleSheet("QPushButton{\n"
"    border-top-left-radius:0px;\n"
"    border-top-right-radius:0px;\n"
"    border-bottom-right-radius:0px;\n"
"    border-bottom-left-radius:0px;\n"
"    color:#928ae1;\n"
"    icon:url(:/svg/mode_purple.svg);\n"
"}    \n"
"\n"
"QPushButton:hover{\n"
"    background-color:rgb(146, 138, 255);\n"
"    border:none;\n"
"    padding: 3px;\n"
"    color: #FFFFFF;\n"
"    icon:url(:/svg/mode_white.svg);\n"
"}\n"
"")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/svg/mode.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mode_choose.setIcon(icon9)
        self.mode_choose.setIconSize(QtCore.QSize(20, 20))
        self.mode_choose.setObjectName("mode_choose")
        self.btn_line = QtWidgets.QPushButton(self.frame_4)
        self.btn_line.setGeometry(QtCore.QRect(140, 0, 71, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_line.setFont(font)
        self.btn_line.setStyleSheet("QPushButton{\n"
"    border-top-left-radius:0px;\n"
"    border-top-right-radius:0px;\n"
"    border-bottom-right-radius:0px;\n"
"    border-bottom-left-radius:0px;\n"
"    color:#928ae1;\n"
"    icon:url(:/svg/line_purple.svg);\n"
"}    \n"
"\n"
"QPushButton:hover{\n"
"    background-color:rgb(146, 138, 255);\n"
"    border:none;\n"
"    padding: 3px;\n"
"    color: #FFFFFF;\n"
"    icon:url(:/svg/line_white.svg);\n"
"}\n"
"")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/svg/line.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_line.setIcon(icon10)
        self.btn_line.setIconSize(QtCore.QSize(20, 20))
        self.btn_line.setObjectName("btn_line")
        self.time_show_label = QtWidgets.QLabel(self.frame_4)
        self.time_show_label.setGeometry(QtCore.QRect(420, 10, 141, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.time_show_label.setFont(font)
        self.time_show_label.setStyleSheet("color:#928ae1;\n"
"")
        self.time_show_label.setText("")
        self.time_show_label.setObjectName("time_show_label")
        self.btn_replay = QtWidgets.QPushButton(self.frame_4)
        self.btn_replay.setGeometry(QtCore.QRect(570, 0, 31, 41))
        self.btn_replay.setStyleSheet("QPushButton{\n"
"    border-top-left-radius:0px;\n"
"    border-top-right-radius:0px;\n"
"    border-bottom-right-radius:0px;\n"
"    border-bottom-left-radius:0px;\n"
"    color:#928ae1;\n"
"    icon:url(:/svg/zhongfang-purple.svg);\n"
"}    \n"
"\n"
"QPushButton:hover{\n"
"    background-color:rgb(146, 138, 255);\n"
"    border:none;\n"
"    padding: 3px;\n"
"    color: #FFFFFF;\n"
"    icon:url(:/svg/zhongfang-white.svg);\n"
"}\n"
"")
        self.btn_replay.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/svg/zhongfang_purple.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_replay.setIcon(icon11)
        self.btn_replay.setIconSize(QtCore.QSize(20, 20))
        self.btn_replay.setObjectName("btn_replay")
        self.frame_3 = QtWidgets.QFrame(self.frame_5)
        self.frame_3.setGeometry(QtCore.QRect(490, 40, 461, 551))
        self.frame_3.setStyleSheet("background-color: #e7e8f0;\n"
"border-top-right-radius:0px;\n"
"border-top-left-radius:0px;\n"
"border-bottom-left-radius:0px;\n"
"border-bottom-right-radius:32px;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_3)
        self.stackedWidget.setGeometry(QtCore.QRect(-1, -1, 461, 281))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.curve_frame = QtWidgets.QFrame(self.page)
        self.curve_frame.setGeometry(QtCore.QRect(0, 0, 461, 281))
        self.curve_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.curve_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.curve_frame.setObjectName("curve_frame")
        self.curve_view = QtWidgets.QGraphicsView(self.curve_frame)
        self.curve_view.setGeometry(QtCore.QRect(0, 0, 461, 281))
        self.curve_view.setStyleSheet("border-top-right-radius:0px;\n"
"border-top-left-radius:0px;\n"
"border-bottom-right-radius:0px;\n"
"border-bottom-left-radius:0px;")
        self.curve_view.setObjectName("curve_view")
        self.stackedWidget.addWidget(self.page)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.stackedWidget.addWidget(self.page_5)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.info_frame = QtWidgets.QFrame(self.page_2)
        self.info_frame.setGeometry(QtCore.QRect(0, 0, 461, 281))
        self.info_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.info_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.info_frame.setObjectName("info_frame")
        self.work_label_5 = QtWidgets.QLabel(self.info_frame)
        self.work_label_5.setGeometry(QtCore.QRect(130, 10, 171, 31))
        self.work_label_5.setStyleSheet("font: 35 12pt \'微软雅黑 Light\';\n"
"color: rgb(255,255,255);\n"
"background-color: rgb(146, 138, 255);\n"
"border: none;border-radius:15px;")
        self.work_label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.work_label_5.setObjectName("work_label_5")
        self.info1 = QtWidgets.QLabel(self.info_frame)
        self.info1.setGeometry(QtCore.QRect(60, 90, 161, 41))
        self.info1.setText("")
        self.info1.setObjectName("info1")
        self.info2 = QtWidgets.QLabel(self.info_frame)
        self.info2.setGeometry(QtCore.QRect(60, 150, 161, 41))
        self.info2.setText("")
        self.info2.setObjectName("info2")
        self.btn_draw_image_save = QtWidgets.QPushButton(self.info_frame)
        self.btn_draw_image_save.setGeometry(QtCore.QRect(280, 120, 131, 31))
        self.btn_draw_image_save.setStyleSheet("QPushButton{\n"
"    border-top-left-radius:0px;\n"
"    border-top-right-radius:0px;\n"
"    border-bottom-right-radius:0px;\n"
"    border-bottom-left-radius:0px;\n"
"    color:#928ae1;\n"
"}    \n"
"\n"
"QPushButton:hover{\n"
"    background-color:rgb(146, 138, 255);\n"
"    border:none;\n"
"    padding: 3px;\n"
"    color: #FFFFFF;\n"
"}\n"
"")
        self.btn_draw_image_save.setObjectName("btn_draw_image_save")
        self.info3 = QtWidgets.QLabel(self.info_frame)
        self.info3.setGeometry(QtCore.QRect(60, 210, 161, 41))
        self.info3.setText("")
        self.info3.setObjectName("info3")
        self.stackedWidget.addWidget(self.page_2)
        self.frame_6 = QtWidgets.QFrame(self.frame_3)
        self.frame_6.setGeometry(QtCore.QRect(-1, 279, 461, 271))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.frame_6)
        self.stackedWidget_2.setGeometry(QtCore.QRect(0, 0, 461, 271))
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.stackedWidget_2.addWidget(self.page_4)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.yingbian_frame = QtWidgets.QFrame(self.page_6)
        self.yingbian_frame.setGeometry(QtCore.QRect(0, 0, 461, 271))
        self.yingbian_frame.setAutoFillBackground(False)
        self.yingbian_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.yingbian_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.yingbian_frame.setObjectName("yingbian_frame")
        self.x_coordinate_2 = QtWidgets.QLineEdit(self.yingbian_frame)
        self.x_coordinate_2.setGeometry(QtCore.QRect(110, 70, 113, 41))
        self.x_coordinate_2.setStyleSheet("QLineEdit {\n"
"  color: rgb(170, 63, 104);\n"
"  padding-left: 8px;\n"
"  border-radius: 0px;\n"
"  border-top-left-radius: 4px;\n"
"  border-top-right-radius: 4px;\n"
"  height: 32px;\n"
"  background-color: #FFFFFF;\n"
"  border: 3px solid rgb(199, 199, 199);\n"
"  border-width: 0 0 3px 0;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"  color: rgb(170, 63, 104);\n"
"  border: 3px solid rgb(170, 63, 104);\n"
"  border-width: 0 0 3px 0;\n"
"}\n"
"")
        self.x_coordinate_2.setText("")
        self.x_coordinate_2.setObjectName("x_coordinate_2")
        self.work_label_2 = QtWidgets.QLabel(self.yingbian_frame)
        self.work_label_2.setGeometry(QtCore.QRect(130, 10, 171, 31))
        self.work_label_2.setStyleSheet("font: 35 12pt \'微软雅黑 Light\';\n"
"color: rgb(255,255,255);\n"
"background-color: rgb(146, 138, 255);\n"
"border: none;border-radius:15px;")
        self.work_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.work_label_2.setObjectName("work_label_2")
        self.y_coordinate_1 = QtWidgets.QLineEdit(self.yingbian_frame)
        self.y_coordinate_1.setGeometry(QtCore.QRect(320, 70, 113, 41))
        self.y_coordinate_1.setStyleSheet("QLineEdit {\n"
"  color: rgb(170, 63, 104);\n"
"  padding-left: 8px;\n"
"  border-radius: 0px;\n"
"  border-top-left-radius: 4px;\n"
"  border-top-right-radius: 4px;\n"
"  height: 32px;\n"
"  background-color: #FFFFFF;\n"
"  border: 3px solid rgb(199, 199, 199);\n"
"  border-width: 0 0 3px 0;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"  color: rgb(170, 63, 104);\n"
"  border: 3px solid rgb(170, 63, 104);\n"
"  border-width: 0 0 3px 0;\n"
"}\n"
"")
        self.y_coordinate_1.setText("")
        self.y_coordinate_1.setObjectName("y_coordinate_1")
        self.x_coordinate_1 = QtWidgets.QLineEdit(self.yingbian_frame)
        self.x_coordinate_1.setGeometry(QtCore.QRect(110, 140, 113, 41))
        self.x_coordinate_1.setStyleSheet("QLineEdit {\n"
"  color: rgb(170, 63, 104);\n"
"  padding-left: 8px;\n"
"  border-radius: 0px;\n"
"  border-top-left-radius: 4px;\n"
"  border-top-right-radius: 4px;\n"
"  height: 32px;\n"
"  background-color: #FFFFFF;\n"
"  border: 3px solid rgb(199, 199, 199);\n"
"  border-width: 0 0 3px 0;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"  color: rgb(170, 63, 104);\n"
"  border: 3px solid rgb(170, 63, 104);\n"
"  border-width: 0 0 3px 0;\n"
"}\n"
"")
        self.x_coordinate_1.setText("")
        self.x_coordinate_1.setObjectName("x_coordinate_1")
        self.y_coordinate_2 = QtWidgets.QLineEdit(self.yingbian_frame)
        self.y_coordinate_2.setGeometry(QtCore.QRect(320, 140, 113, 41))
        self.y_coordinate_2.setStyleSheet("QLineEdit {\n"
"  color: rgb(170, 63, 104);\n"
"  padding-left: 8px;\n"
"  border-radius: 0px;\n"
"  border-top-left-radius: 4px;\n"
"  border-top-right-radius: 4px;\n"
"  height: 32px;\n"
"  background-color: #FFFFFF;\n"
"  border: 3px solid rgb(199, 199, 199);\n"
"  border-width: 0 0 3px 0;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"  color: rgb(170, 63, 104);\n"
"  border: 3px solid rgb(170, 63, 104);\n"
"  border-width: 0 0 3px 0;\n"
"}\n"
"")
        self.y_coordinate_2.setText("")
        self.y_coordinate_2.setObjectName("y_coordinate_2")
        self.label_9 = QtWidgets.QLabel(self.yingbian_frame)
        self.label_9.setGeometry(QtCore.QRect(10, 80, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.yingbian_frame)
        self.label_10.setGeometry(QtCore.QRect(10, 150, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_12 = QtWidgets.QLabel(self.yingbian_frame)
        self.label_12.setGeometry(QtCore.QRect(230, 80, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_15 = QtWidgets.QLabel(self.yingbian_frame)
        self.label_15.setGeometry(QtCore.QRect(230, 140, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.btn_confirm_1 = QtWidgets.QPushButton(self.yingbian_frame)
        self.btn_confirm_1.setGeometry(QtCore.QRect(270, 200, 101, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_confirm_1.setFont(font)
        self.btn_confirm_1.setStyleSheet("QPushButton{\n"
"    border-top-left-radius:0px;\n"
"    border-top-right-radius:0px;\n"
"    border-bottom-right-radius:0px;\n"
"    border-bottom-left-radius:0px;\n"
"    color:#928ae1;\n"
"}    \n"
"\n"
"QPushButton:hover{\n"
"    background-color:rgb(146, 138, 255);\n"
"    border:none;\n"
"    padding: 3px;\n"
"    color: #FFFFFF;\n"
"}\n"
"")
        self.btn_confirm_1.setIcon(icon5)
        self.btn_confirm_1.setIconSize(QtCore.QSize(20, 20))
        self.btn_confirm_1.setObjectName("btn_confirm_1")
        self.stackedWidget_2.addWidget(self.page_6)
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.edit_frame = QtWidgets.QFrame(self.page_1)
        self.edit_frame.setGeometry(QtCore.QRect(0, 0, 461, 271))
        self.edit_frame.setAutoFillBackground(False)
        self.edit_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.edit_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.edit_frame.setObjectName("edit_frame")
        self.work_label_3 = QtWidgets.QLabel(self.edit_frame)
        self.work_label_3.setGeometry(QtCore.QRect(130, 10, 171, 31))
        self.work_label_3.setStyleSheet("font: 35 12pt \'微软雅黑 Light\';\n"
"color: rgb(255,255,255);\n"
"background-color: rgb(146, 138, 255);\n"
"border: none;border-radius:15px;")
        self.work_label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.work_label_3.setObjectName("work_label_3")
        self.label_13 = QtWidgets.QLabel(self.edit_frame)
        self.label_13.setGeometry(QtCore.QRect(43, 110, 91, 31))
        self.label_13.setObjectName("label_13")
        self.btn_color = QtWidgets.QPushButton(self.edit_frame)
        self.btn_color.setGeometry(QtCore.QRect(270, 110, 81, 31))
        self.btn_color.setStyleSheet("QPushButton{\n"
"    border-top-left-radius:0px;\n"
"    border-top-right-radius:0px;\n"
"    border-bottom-right-radius:0px;\n"
"    border-bottom-left-radius:0px;\n"
"    color:#928ae1;\n"
"}    \n"
"\n"
"QPushButton:hover{\n"
"    background-color:rgb(146, 138, 255);\n"
"    border:none;\n"
"    padding: 3px;\n"
"    color: #FFFFFF;\n"
"}\n"
"")
        self.btn_color.setObjectName("btn_color")
        self.color_show = QtWidgets.QFrame(self.edit_frame)
        self.color_show.setGeometry(QtCore.QRect(170, 110, 61, 31))
        self.color_show.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.color_show.setFrameShadow(QtWidgets.QFrame.Raised)
        self.color_show.setObjectName("color_show")
        self.recall_btn = QtWidgets.QPushButton(self.edit_frame)
        self.recall_btn.setGeometry(QtCore.QRect(70, 200, 81, 31))
        self.recall_btn.setStyleSheet("QPushButton{\n"
"    border-top-left-radius:0px;\n"
"    border-top-right-radius:0px;\n"
"    border-bottom-right-radius:0px;\n"
"    border-bottom-left-radius:0px;\n"
"    color:#928ae1;\n"
"}    \n"
"\n"
"QPushButton:hover{\n"
"    background-color:rgb(146, 138, 255);\n"
"    border:none;\n"
"    padding: 3px;\n"
"    color: #FFFFFF;\n"
"}\n"
"")
        self.recall_btn.setObjectName("recall_btn")
        self.restore_btn = QtWidgets.QPushButton(self.edit_frame)
        self.restore_btn.setGeometry(QtCore.QRect(270, 200, 81, 31))
        self.restore_btn.setStyleSheet("QPushButton{\n"
"    border-top-left-radius:0px;\n"
"    border-top-right-radius:0px;\n"
"    border-bottom-right-radius:0px;\n"
"    border-bottom-left-radius:0px;\n"
"    color:#928ae1;\n"
"}    \n"
"\n"
"QPushButton:hover{\n"
"    background-color:rgb(146, 138, 255);\n"
"    border:none;\n"
"    padding: 3px;\n"
"    color: #FFFFFF;\n"
"}\n"
"")
        self.restore_btn.setObjectName("restore_btn")
        self.stackedWidget_2.addWidget(self.page_1)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.yingli_frame = QtWidgets.QFrame(self.page_3)
        self.yingli_frame.setGeometry(QtCore.QRect(0, 0, 461, 271))
        self.yingli_frame.setAutoFillBackground(False)
        self.yingli_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.yingli_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.yingli_frame.setObjectName("yingli_frame")
        self.work_label = QtWidgets.QLabel(self.yingli_frame)
        self.work_label.setGeometry(QtCore.QRect(130, 10, 171, 31))
        self.work_label.setStyleSheet("font: 35 12pt \'微软雅黑 Light\';\n"
"color: rgb(255,255,255);\n"
"background-color: rgb(146, 138, 255);\n"
"border: none;border-radius:15px;")
        self.work_label.setAlignment(QtCore.Qt.AlignCenter)
        self.work_label.setObjectName("work_label")
        self.diameter_input = QtWidgets.QLineEdit(self.yingli_frame)
        self.diameter_input.setGeometry(QtCore.QRect(80, 80, 113, 41))
        self.diameter_input.setStyleSheet("QLineEdit {\n"
"  color: rgb(170, 63, 104);\n"
"  padding-left: 8px;\n"
"  border-radius: 0px;\n"
"  border-top-left-radius: 4px;\n"
"  border-top-right-radius: 4px;\n"
"  height: 32px;\n"
"  background-color: #FFFFFF;\n"
"  border: 3px solid rgb(199, 199, 199);\n"
"  border-width: 0 0 3px 0;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"  color: rgb(170, 63, 104);\n"
"  border: 3px solid rgb(170, 63, 104);\n"
"  border-width: 0 0 3px 0;\n"
"}\n"
"")
        self.diameter_input.setText("")
        self.diameter_input.setObjectName("diameter_input")
        self.constant_input = QtWidgets.QLineEdit(self.yingli_frame)
        self.constant_input.setGeometry(QtCore.QRect(260, 80, 113, 41))
        self.constant_input.setStyleSheet("QLineEdit {\n"
"  color: rgb(170, 63, 104);\n"
"  padding-left: 8px;\n"
"  border-radius: 0px;\n"
"  border-top-left-radius: 4px;\n"
"  border-top-right-radius: 4px;\n"
"  height: 32px;\n"
"  background-color: #FFFFFF;\n"
"  border: 3px solid rgb(199, 199, 199);\n"
"  border-width: 0 0 3px 0;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"  color: rgb(170, 63, 104);\n"
"  border: 3px solid rgb(170, 63, 104);\n"
"  border-width: 0 0 3px 0;\n"
"}\n"
"")
        self.constant_input.setText("")
        self.constant_input.setObjectName("constant_input")
        self.scale_input = QtWidgets.QLineEdit(self.yingli_frame)
        self.scale_input.setGeometry(QtCore.QRect(80, 150, 113, 41))
        self.scale_input.setStyleSheet("QLineEdit {\n"
"  color: rgb(170, 63, 104);\n"
"  padding-left: 8px;\n"
"  border-radius: 0px;\n"
"  border-top-left-radius: 4px;\n"
"  border-top-right-radius: 4px;\n"
"  height: 32px;\n"
"  background-color: #FFFFFF;\n"
"  border: 3px solid rgb(199, 199, 199);\n"
"  border-width: 0 0 3px 0;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"  color: rgb(170, 63, 104);\n"
"  border: 3px solid rgb(170, 63, 104);\n"
"  border-width: 0 0 3px 0;\n"
"}\n"
"")
        self.scale_input.setText("")
        self.scale_input.setObjectName("scale_input")
        self.scale_input2 = QtWidgets.QLineEdit(self.yingli_frame)
        self.scale_input2.setGeometry(QtCore.QRect(260, 150, 113, 41))
        self.scale_input2.setStyleSheet("QLineEdit {\n"
"  color: rgb(170, 63, 104);\n"
"  padding-left: 8px;\n"
"  border-radius: 0px;\n"
"  border-top-left-radius: 4px;\n"
"  border-top-right-radius: 4px;\n"
"  height: 32px;\n"
"  background-color: #FFFFFF;\n"
"  border: 3px solid rgb(199, 199, 199);\n"
"  border-width: 0 0 3px 0;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"  color: rgb(170, 63, 104);\n"
"  border: 3px solid rgb(170, 63, 104);\n"
"  border-width: 0 0 3px 0;\n"
"}\n"
"")
        self.scale_input2.setText("")
        self.scale_input2.setObjectName("scale_input2")
        self.label_2 = QtWidgets.QLabel(self.yingli_frame)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 41, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.yingli_frame)
        self.label_3.setGeometry(QtCore.QRect(10, 150, 71, 41))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.yingli_frame)
        self.label_5.setGeometry(QtCore.QRect(210, 90, 41, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.yingli_frame)
        self.label_6.setGeometry(QtCore.QRect(220, 150, 16, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.btn_confirm_2 = QtWidgets.QPushButton(self.yingli_frame)
        self.btn_confirm_2.setGeometry(QtCore.QRect(260, 210, 101, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_confirm_2.setFont(font)
        self.btn_confirm_2.setStyleSheet("QPushButton{\n"
"    border-top-left-radius:0px;\n"
"    border-top-right-radius:0px;\n"
"    border-bottom-right-radius:0px;\n"
"    border-bottom-left-radius:0px;\n"
"    color:#928ae1;\n"
"}    \n"
"\n"
"QPushButton:hover{\n"
"    background-color:rgb(146, 138, 255);\n"
"    border:none;\n"
"    padding: 3px;\n"
"    color: #FFFFFF;\n"
"}\n"
"")
        self.btn_confirm_2.setIcon(icon5)
        self.btn_confirm_2.setIconSize(QtCore.QSize(20, 20))
        self.btn_confirm_2.setObjectName("btn_confirm_2")
        self.stackedWidget_2.addWidget(self.page_3)
        self.frame_2 = QtWidgets.QFrame(self.frame_5)
        self.frame_2.setGeometry(QtCore.QRect(0, 40, 491, 551))
        self.frame_2.setStyleSheet("background-color: #e7e8f0;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.video_label = QtWidgets.QGraphicsView(self.frame_2)
        self.video_label.setGeometry(QtCore.QRect(0, 0, 491, 551))
        self.video_label.setStyleSheet("border-top-left-radius:0px;\n"
"border-top-right-radius:0px;\n"
"border-bottom-right-radius:0px;\n"
"border-bottom-left-radius:0px;")
        self.video_label.setObjectName("video_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1307, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        self.stackedWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.inter_tilte.setText(_translate("MainWindow", " 纳米材料力学性能分析"))
        self.label_8.setText(_translate("MainWindow", "文件属性"))
        self.btn_rect.setText(_translate("MainWindow", "矩形"))
        self.btn_circle.setText(_translate("MainWindow", "椭圆"))
        self.btn_curve.setText(_translate("MainWindow", "曲线"))
        self.btn_select.setText(_translate("MainWindow", "文件"))
        self.mode_choose.setText(_translate("MainWindow", "模式"))
        self.btn_line.setText(_translate("MainWindow", "直线"))
        self.work_label_5.setText(_translate("MainWindow", "信息区"))
        self.btn_draw_image_save.setText(_translate("MainWindow", "保存绘制后图片"))
        self.x_coordinate_2.setPlaceholderText(_translate("MainWindow", "x"))
        self.work_label_2.setText(_translate("MainWindow", "设置区"))
        self.y_coordinate_1.setPlaceholderText(_translate("MainWindow", "y"))
        self.x_coordinate_1.setPlaceholderText(_translate("MainWindow", "x"))
        self.y_coordinate_2.setPlaceholderText(_translate("MainWindow", "y"))
        self.label_9.setText(_translate("MainWindow", "点1横坐标："))
        self.label_10.setText(_translate("MainWindow", "点2横坐标："))
        self.label_12.setText(_translate("MainWindow", "点1纵坐标："))
        self.label_15.setText(_translate("MainWindow", "点2纵坐标："))
        self.btn_confirm_1.setText(_translate("MainWindow", "确定"))
        self.work_label_3.setText(_translate("MainWindow", "设置区"))
        self.label_13.setText(_translate("MainWindow", "画笔颜色:"))
        self.btn_color.setText(_translate("MainWindow", "更改颜色"))
        self.recall_btn.setText(_translate("MainWindow", "撤回操作"))
        self.restore_btn.setText(_translate("MainWindow", "恢复操作"))
        self.work_label.setText(_translate("MainWindow", "设置区"))
        self.diameter_input.setPlaceholderText(_translate("MainWindow", "直径"))
        self.constant_input.setPlaceholderText(_translate("MainWindow", "常数"))
        self.scale_input.setPlaceholderText(_translate("MainWindow", "纳米数"))
        self.scale_input2.setPlaceholderText(_translate("MainWindow", "对应像素数"))
        self.label_2.setText(_translate("MainWindow", "直径："))
        self.label_3.setText(_translate("MainWindow", "比例尺："))
        self.label_5.setText(_translate("MainWindow", "常数："))
        self.label_6.setText(_translate("MainWindow", ":"))
        self.btn_confirm_2.setText(_translate("MainWindow", "确定"))
