import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt, QRect, pyqtSignal, pyqtSlot

class thermo(QWidget):
    colorChanged=pyqtSignal(int)
    valueChanged=pyqtSignal(int)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.radius=20
        self.height=80 #selfmax-selfmin
        self.width=self.radius
        self.color=Qt.green
        self.value=25
        self.h=self.value
        self.max=60
        self.min=-20
        self.froid=0
        self.chaud=30
        self.initGui() 
        #après avoir défini les caractéristiques de notre thermomètre
        #nous appelons notre fonction initialisation graphique qui
        #spécifie la dimension de l'objet
    def setTemp(self,val):  #fonction setter permet de modifier la
        self.value=val      #valeur de la température depuis 
        self.update()       #l'extérieur de l'objet
    def initGui(self):
        self.setGeometry(0, 0, 4*self.radius, 4*self.radius + self.height)
        self.show
    def paintEvent(self, event):
        qp=QPainter()
        qp.begin(self)
        pen=QPen()
        pen.setWidth(1)
        pen.setColor(Qt.white)
        qp.setPen(pen)
        qp.setBrush(Qt.white)
        qp.drawRect(int(self.radius/2), 5, self.width, self.height + self.radius)
        if self.value < self.froid:
            pen.setColor(Qt.blue)
            qp.setPen(pen)
            qp.setBrush(Qt.blue)
        elif self.value > self.chaud:
            pen.setColor(Qt.red)
            qp.setPen(pen)
            qp.setBrush(Qt.red)
        else:
             pen.setColor(Qt.green)
             qp.setPen(pen)
             qp.setBrush(Qt.green)
        #qp.drawEllipse(-40,100, self.height + 2 * self.radius, 2 * self.radius)
        qp.drawEllipse(0, self.height , 2 * self.radius, 2 * self.radius)
        qp.drawRect(int(self.radius/2), self.height + 20 + 5, self.width,-(5 + self.radius) - self.value)
        #Pour l'affichage textuel de la température
        #spécifions la couleur, taille des caractères
        pen.setColor(Qt.black)
        qp.setPen(pen)
        qp.setFont(QFont('Arial',12))
        qp.drawText(int(self.radius / 2), (self.height+2*self.radius+5), str(self.value))
        qp.end()
        #visuel du thermometre avec les valeurs emit = signaux
    def changeCouleur(self, color):
        self.color = color
        self.colorChanged.emit(self.color)
        self.update()
    def changeValeur(self, value):
        self.value = value
        self.valueChanged.emit(self.value)
        self.h = self.value+20
        self.update()








