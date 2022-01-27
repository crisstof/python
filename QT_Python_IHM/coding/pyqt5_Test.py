import sys
from PyQt5.QtWidgets import QApplication, QGridLayout, QLabel, QPushButton, QWidget
from PyQt5.QtGui import *

class fenetre_principale(QWidget):
    def __init__(self):
        super().__init__()
        self.InitGUI()
    def InitGUI(self):
        self.setWindowTitle('Bonjour')
        self.resize(500, 500)
        self.layout=QGridLayout()
        self.bouton1=QPushButton("1")
        self.bouton1.clicked.connect(self.bouton)
        self.bouton2=QPushButton("2")
        self.bouton2.clicked.connect(self.bouton)
        self.bouton3=QPushButton('3', None)
        self.bouton3.clicked.connect(self.bouton)
        self.layout.addWidget(self.bouton1, 0, 0, 1, 2)
        self.layout.addWidget(self.bouton2,0,3)
        self.layout.addWidget(self.bouton3,2,2)
        self.setLayout(self.layout)
        self.show()
    def bouton(self):
        sender=self.sender()
        print(f'Paul à appuyé sur le Bouton {sender.text()} ')
        
if __name__=='__main__':
    app=QApplication(sys.argv) #Gère l'aspet évènementiel du prog (1 seule instance)
    IHM=fenetre_principale()
    app.exec_()  #reste ouvert



