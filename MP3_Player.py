import numpy
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from pathlib import Path
from pygame import mixer

global opensong
global song
mixer.init()
n = 0
scopy = []
scopy1 = []
class Player(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('MP3 Player')
        self.setFixedSize(1480, 400)
        self.bg = QLabel(self)
        self.bg.setPixmap(QPixmap('mp3_bg.jpg'))
        self.bg.adjustSize()
        self.setWindowIcon(QIcon('icon_player.png'))

        # song name
        self.nm = QTextEdit(self)
        self.nm.setFont(QFont('Berlin Sans FB Demi', 44))
        self.nm.setStyleSheet("color: white; background-image: url(mp3_bg.jpg); border: 0")
        self.nm.move(0, 0)
        self.nm.setFixedSize(1000, 180)
        self.nm.setReadOnly(True)

        # Developers
        self.d = QLabel('Developed by Aayush & Yukta', self)
        self.d.setFont(QFont('Berlin Sans FB Demi', 12))
        self.d.setStyleSheet('color: white')
        self.d.adjustSize()
        self.d.move(10, 360)

        # song select button
        self.select = QPushButton(self)
        self.select.setStyleSheet('background-color: transparent; border-radius: 40')
        self.select.setIcon(QIcon('select.png'))
        self.select.setIconSize(QtCore.QSize(200, 200))
        self.select.adjustSize()
        self.select.move(720, 240)
        self.select.clicked.connect(lambda: self.selectsong())

        # play button
        self.play1()

        # next button
        self.next = QPushButton(self)
        self.next.setStyleSheet('background-color: transparent; border-radius: 40')
        self.next.setIcon(QIcon('next.png'))
        self.next.setIconSize(QtCore.QSize(80, 80))
        self.next.setFixedSize(100, 100)
        self.next.move(580, 280)
        self.next.clicked.connect(lambda: self.next1())
        # prev button
        self.prev = QPushButton(self)
        self.prev.setStyleSheet('background-color: transparent; border-radius: 40')
        self.prev.setIcon(QIcon('prev.png'))
        self.prev.setIconSize(QtCore.QSize(80, 80))
        self.prev.setFixedSize(100, 100)
        self.prev.move(380, 280)
        self.prev.clicked.connect(lambda: self.prev1())
        # queue
        self.queue = QTextEdit(self)
        self.queue.setFixedSize(400, 280)
        self.queue.move(1000, 40)
        self.queue.setReadOnly(True)
        self.queue.setFont(QFont('Berlin Sans FB Demi', 14))
        self.queue.setStyleSheet('background: black; color: white; border-radius: 20')
        self.show()

    def play1(self):
        self.play = QPushButton(self)
        self.play.setStyleSheet('background-color: transparent; border-radius: 40')
        self.play.setIcon(QIcon('play.png'))
        self.play.setIconSize(QtCore.QSize(80, 80))
        self.play.setFixedSize(100, 100)
        self.play.move(480, 280)
        mixer.music.set_volume(0.8)
        mixer.music.pause()
        self.play.clicked.connect(lambda: self.pause1())
        self.play.show()

    def pause1(self):
        self.play.destroy(True)
        self.pause = QPushButton(self)
        self.pause.setStyleSheet('background-color: transparent; border-radius: 40')
        self.pause.setIcon(QIcon('pause.png'))
        self.pause.setIconSize(QtCore.QSize(80, 80))
        self.pause.setFixedSize(100, 100)
        self.pause.move(480, 280)
        mixer.music.set_volume(0.8)
        mixer.music.unpause()
        self.pause.show()
        self.pause.clicked.connect(lambda: self.play1())

    def selectsong(self):
        global n
        global opensongl
        global scopy
        self.nm.clear()
        global opensong
        global filenm
        global scopy1
        opensong = QFileDialog.getOpenFileNames(self, "Select Song", "",  "Mp3 Files (*.mp3)")
        opensong = (opensong[0])
        scopy.append(opensong)
        # flatten the list
        scopy1 = list(numpy.concatenate(scopy).flat)
        print("Sorted:", scopy1)
        opensong_s = str(scopy1[n])
        filenm = Path(opensong_s).stem
        for i in range(0, len(opensong)):
            qname = Path(opensong[i]).stem
            self.queue.insertPlainText(qname + '\n\n')
        filenm = str(filenm)
        self.nm.insertPlainText(filenm)
        self.nm.setAlignment(QtCore.Qt.AlignCenter)
        self.nm.setReadOnly(True)
        print(filenm)
        mixer.music.load(filename=scopy1[n])
        mixer.music.set_volume(0)
        mixer.music.play()
        mixer.music.pause()

    def next1(self):
        global n
        global opensong
        global filenm
        global scopy1
        n += 1
        self.nm.clear()
        opensong_s = str(scopy1[n])
        filenm = Path(opensong_s).stem
        self.nm.insertPlainText(filenm)
        self.nm.setAlignment(QtCore.Qt.AlignCenter)
        self.nm.setReadOnly(True)
        mixer.music.load(filename=scopy1[n])
        mixer.music.set_volume(0.8)
        mixer.music.play()
        print(n)

    def prev1(self):
        global n
        global opensong
        global scopy
        n -= 1
        self.nm.clear()
        opensong_s = str(scopy1[n])
        filenm = Path(opensong_s).stem
        self.nm.insertPlainText(filenm)
        self.nm.setAlignment(QtCore.Qt.AlignCenter)
        self.nm.setReadOnly(True)
        mixer.music.load(filename=scopy1[n])
        mixer.music.set_volume(0.8)
        mixer.music.play()
        print(n)


player = QApplication([])
p = Player()
p.show()
player.exec_()