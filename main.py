import sys

from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt
import pyautogui


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setAutoFillBackground(True)
        self.setAttribute(Qt.WA_NoSystemBackground, False)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setAttribute(Qt.WA_TransparentForMouseEvents, False)
        # self.setWindowFlags(Qt.Window)
        self.setWindowFlags(Qt.FramelessWindowHint)
        pyautogui.click(1769, 20)
        self.draw = True
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Clicker')
        self.showFullScreen()

    def mousePressEvent(self, event):
        global points
        x = event.x()
        y = event.y()
        print(x, y)
        points.append((x, y))
        self.update()

    def paintEvent(self, event):
        global height, width, points
        qp = QPainter()
        qp.begin(self)
        if self.draw:
            qp.setBrush(QColor(255, 255, 255, 100))
            qp.drawRect(0, 0, width, height)
            pen = QPen(QColor(255, 0, 0, 100), 20, Qt.SolidLine)
            qp.setPen(pen)
            for i in points:
                qp.drawPoint(*i)
        qp.end()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()
        elif event.key() == Qt.Key_Space:
            self.draw = False
            self.paintEvent(None)
            self.update()
            closing()
            self.close()
    #
    # def draw(self):
    #     pass


def closing():
    global points
    for _ in range(10):
        for i in points:
            pyautogui.click(*i)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    points = []
    height, width = app.primaryScreen().size().height(), app.primaryScreen().size().width()
    mw = MyWindow()
    sys.exit(app.exec_())
