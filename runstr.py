import cv2
import numpy as np
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class wind(QMainWindow):
    def __init__(self):
        super(wind, self).__init__()

        self.setWindowTitle("Running str")
        self.setGeometry(500, 400, 400, 300)

        #label 1
        self.main_text = QtWidgets.QLabel(self)
        self.main_text.setText("Введите текст бегущей строки")
        self.main_text.move(10, 60)
        self.main_text.adjustSize()

        #label 2
        self.main_text = QtWidgets.QLabel(self)
        self.main_text.setText("Выберите цвет текста")
        self.main_text.move(10, 100)
        self.main_text.adjustSize()


        
        #fc1
        self.btn1 = QtWidgets.QPushButton(self)
        self.btn1.move(180, 90)
        self.btn1.setFixedWidth(30)
        self.btn1.setStyleSheet('background: rgb(255,153, 153);')
        self.btn1.clicked.connect(self.set_font_color1)
        #fc2
        self.btn2 = QtWidgets.QPushButton(self)
        self.btn2.move(220, 90)
        self.btn2.setFixedWidth(30)
        self.btn2.setStyleSheet('background: rgb(153, 255, 153);')
        self.btn2.clicked.connect(self.set_font_color2)
        #fc3
        self.btn3 = QtWidgets.QPushButton(self)
        self.btn3.move(260, 90)
        self.btn3.setFixedWidth(30)
        self.btn3.setStyleSheet('background: rgb(153, 153, 255);')
        self.btn3.clicked.connect(self.set_font_color3)

        #label 2
        self.main_text = QtWidgets.QLabel(self)
        self.main_text.setText("Выберите цвет фона")
        self.main_text.move(10, 150)
        self.main_text.adjustSize()

        self.font_color = (0,0,0)

        self.set_bg = 0
    
        #bg1
        self.btn4 = QtWidgets.QPushButton(self)
        self.btn4.move(180, 140)
        self.btn4.setFixedWidth(30)
        self.btn4.setStyleSheet('background: rgb(153,153, 0);')
        self.btn4.clicked.connect(self.set_bg1)
        #bg2
        self.btn5 = QtWidgets.QPushButton(self)
        self.btn5.move(220, 140)
        self.btn5.setFixedWidth(30)
        self.btn5.setStyleSheet('background: rgb(32, 32, 32);')
        self.btn5.clicked.connect(self.set_bg2)
        #bg3
        self.btn6 = QtWidgets.QPushButton(self)
        self.btn6.move(260, 140)
        self.btn6.setFixedWidth(30)
        self.btn6.setStyleSheet('background: rgb(102, 0, 102);')
        self.btn6.clicked.connect(self.set_bg3)

        #input 1
        self.in_text = QtWidgets.QTextEdit(self)
        self.in_text.move(180, 50)
        self.in_text.setFixedWidth(200)
     
        self.fv = ""
        
        #mp4
        self.btn7 = QtWidgets.QPushButton(self)
        self.btn7.move(10, 10)
        self.btn7.setText("MP4")
        self.btn7.setFixedWidth(50)
        self.btn7.clicked.connect(self.fv_mp4)
        self.btn7.clicked.connect(self.run_str)

        #avi
        self.btn8 = QtWidgets.QPushButton(self)
        self.btn8.move(70, 10)
        self.btn8.setText("AVI")
        self.btn8.setFixedWidth(50)
        self.btn8.clicked.connect(self.fv_avi)
        self.btn8.clicked.connect(self.run_str)
    def set_bg1(self):
        self.set_bg = 0
    def set_bg2(self):
        self.set_bg = 1
    def set_bg3(self):
        self.set_bg = 2
    def set_font_color1(self):
        self.font_color = (255,153, 153)
    def set_font_color2(self):
        self.font_color = (153, 255, 153)
    def set_font_color3(self):
        self.font_color = (153, 153, 255)
    def fv_mp4(self):
        self.fv = "mp4"
    def fv_avi(self):
        self.fv = "avi"
        
    def run_str(self):
        w, h = 100, 100
        fr = 24
        text = self.in_text.toPlainText()
        print(text)
        if self.fv == "mp4":
            out = cv2.VideoWriter("runstr.mp4", cv2.VideoWriter_fourcc(*'mp4v'), fr, (w, h))
        if self.fv == "avi":
            out = cv2.VideoWriter("runstr.avi", cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), fr, (w, h))
        #out = cv2.VideoWriter("runstr.mp4", cv2.VideoWriter_fourcc(*'mp4v'), fr, (w, h))
        frame = np.zeros((h, w, 3), dtype = np.uint8)

        y = h // 2

        x = w // 2

        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 1
        font_thickness = 2

        arr = np.array_split(frame, 3, axis=2)
        for t in range(fr*3):
            if self.set_bg == 0:
                arr[0].fill(153)
                arr[1].fill(153)
                arr[2].fill(0)
            if self.set_bg == 1:
                arr[0].fill(32)
                arr[1].fill(32)
                arr[2].fill(32)
            if self.set_bg == 2:
                arr[0].fill(102)
                arr[1].fill(0)
                arr[2].fill(102)
            frame = np.concatenate([arr[0],arr[1],arr[2]], axis=2)
            cv2.putText(frame, text, (x,y), font, font_scale, self.font_color, font_thickness)
            x -= len(text)*8 // fr
        

            out.write(frame)
        out.release()


def application():
    app = QApplication(sys.argv)
    window = wind()

    window.show()
    sys.exit(app.exec_())

application()
