import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget,QVBoxLayout
from PyQt5.QtGui import QPainter,QColor, QFont
from PyQt5.QtCore import Qt

class BlackSquareApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.status_text = "Нет файла" # инициализация status_text
        self.track_name = "Неизвестно"

        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAutoFillBackground(False)

    def initUI(self):
        self.setGeometry(100,100,600,200)
        self.setWindowTitle('2023.08')
        self.setFixedHeight(200)
        self.setFixedWidth(600)

        self.setWindowFlags(Qt.FramelessWindowHint)
        
        layout = QVBoxLayout(self)
        self.setLayout(layout)

    def mousePressEvent(self,event):
        if event.button() == Qt.LeftButton:
            self.dragging = True
            self.offset = event.pos()
    
    def mouseMoveEvent(self, event):
        if self.dragging:
            self.move(event.globalPos() - self.offset)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragging = False

    def paintEvent(self,event):
        painter = QPainter(self)
        #painter.fillRect(event.rect(),QColor(0,0,0))

        square_size=150
        square_x = (self.width() - square_size) // 2
        square_y = (self.height() - square_size) // 2

        corner_radius = 10
        painter.setBrush(QColor(0,0,0))
        painter.drawRoundedRect(0,0,550,200,corner_radius,corner_radius)
        #painter.fillRect(square_x,square_y,square_size,square_size,QColor(0,0,0)) реализовать интерфейс для win 10 и остальных

        text=self.status_text
        font = QFont("Arial",12)
        painter.setFont(font)
        painter.setPen(QColor(255,255,255))
        painter.drawText(square_x-50,(square_y-square_size//8)+50,200,30,Qt.AlignCenter,text)

        text2=self.track_name
        painter.drawText(square_x-50,(square_y-square_size//8)+80,200,30,Qt.AlignCenter,text2)

def create(status_text,track_name):
    app = QApplication(sys.argv)
    ex = BlackSquareApp()
    ex.status_text = status_text #Установка значения атрибута status text в классе blacksquare
    ex.track_name = track_name
    ex.show()
    sys.exit(app.exec_())

if __name__=="__main__":
    create('Проверка статуса','Проверка имени')