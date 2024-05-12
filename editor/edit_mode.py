from editor.edit_kind import EditKind
from editor.point import PointInt
from PyQt5.QtWidgets import (
    QGraphicsView,
    QMessageBox,
    QColorDialog,
)
from PyQt5.QtGui import QMouseEvent, QColor
from PyQt5.QtCore import pyqtSignal
from editor.oprecord import OPRecord

class Editor(QGraphicsView):

    actionChanged = pyqtSignal()
    def __init__(self, raw_view):
        super().__init__()
        self.drawing = False
        self.drawing_id = '0'
        self.drawing_type = 'freenom'
        self.drawing_record = OPRecord(self)
        self.drawing_record_save = 0
        self.drawing_set = None

        self.main_window = None
        self.setGeometry(raw_view.geometry())
        self.setObjectName(raw_view.objectName())
        self.setParent(raw_view.parent())
        raw_view.deleteLater()


        self.color = QColor(0, 0, 0)

    def start(self, type):
        self.drawing_id = self.main_window.get_id(self.drawing_set != None)
        self.drawing_type, self.drawing_set = type, None
        return True

    def mousePressEvent(self, event: QMouseEvent) -> None:
        if self.drawing:
            position = self.mapToScene(event.localPos().toPoint())
            x, y = int(position.x()), int(position.y())
            if self.drawing_set:
                self.drawing_set.p_list.append(PointInt(x, y))
            else:
                self.drawing_set = EditKind(self.drawing_id, self.drawing_type, [PointInt(x, y), PointInt(x, y)], self.color)
                self.drawing_record.do(self.drawing_set)
            text1 = '起点坐标： ({}, {})'.format(self.drawing_set.p_list[0].x, self.drawing_set.p_list[0].y)
            self.main_window.info1.setText(text1)
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        if self.drawing:
            position = self.mapToScene(event.localPos().toPoint())
            x, y = int(position.x()), int(position.y())
            if x < 0 :
                x = 1
            elif x > self.main_window.nw:
                x = self.main_window.nw - 1
            if y < 0:
                y = 1
            elif y > self.main_window.nh:
                y = self.main_window.nh - 1

            if self.drawing_type == "freenom":
                self.drawing_set.p_list.append(PointInt(x, y))
            else:
                self.drawing_set.p_list[-1] = PointInt(x, y)
            self.updateScene([self.sceneRect()])
            now_point = PointInt(x, y)
            start_point = PointInt(self.drawing_set.p_list[0].x, self.drawing_set.p_list[0].y)
            text2 = '当前点坐标： ({}, {})'.format(x, y)
            self.main_window.info2.setText(text2)
            distance = start_point.distance(now_point)
            text3 = '当前点与起点的距离： {}'.format(distance)
            self.main_window.info3.setText(text3)
            super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        if self.drawing:
            self.main_window.modified = True
            if self.drawing_record.finish():
                self.drawing_set = None

            self.drawing_id = self.main_window.get_id(self.drawing_type in EditKind.INC)
            super().mouseReleaseEvent(event)

