from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer, Qt
from psutil import sensors_battery
from pyqtSignal import thermo

from matplotlib import pyplot as plot
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import sys
import random
import numpy as np
import psutil

#Création de la fenêtre + setter+getter + objet sur la fenêtre
class Monitoring(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.status =0
        self.course = 0
    #variables servant à la simulation du tracé de l'historique
        self.tabval = []
        self.Index = 0
        self.InitGUI() 
        #definition de la fonction affiche
    #ajout des setters fonction de modification depuis l'ext class
    def setPval(self, val):
        self.Pstatus.setValue(val)
    def setHval(self,val):
        self.Hstatus.setValue(val)
    def setRSSI(self,val):
        self.RSSIstatus.setValue(val)
    def setTemp(self, val):
        self.thermo.setTemp(val)
    def InitGUI(self):
        self.base = QWidget()
        self.base.setWindowTitle("Station météo")
        self.base.resize(800,540)
    #creation des 2 onglets
        self.tab=QTabWidget()
        self.tab1=QWidget()
        self.tab2=QWidget()
        self.tab.addTab(self.tab1,"Infos")
        self.tab.addTab(self.tab2,"Historique")
        self.mainLayout=QGridLayout()
        self.mainLayout.addWidget(self.tab)
    #définissons et positionnons les objets présents sur l'onglet infos
        self.bt1=QPushButton("OK")
        self.Pstatus=QProgressBar()
        self.Hstatus=QProgressBar()
        self.RSSIstatus=QProgressBar()
        self.thermo=thermo()
        self.Plabel=QLabel('Pression')
        self.Hlabel=QLabel('Humidité')
        self.RSSIlabel=QLabel('RSSI')
        self.infolayout=QGridLayout()
        self.infolayout.addWidget(self.Plabel,0,0)#y,x
        self.infolayout.addWidget(self.Hlabel,1,0)
        self.infolayout.addWidget(self.RSSIlabel,2,0)
        self.infolayout.addWidget(self.Pstatus,0,1)
        self.infolayout.addWidget(self.Hstatus,1,1)
        self.infolayout.addWidget(self.RSSIstatus,2,1)
        self.infolayout.setHorizontalSpacing(20)
        self.infolayout.addWidget(self.thermo,0,3,3,1)
        self.infolayout.addWidget(self.bt1,3,3)
        self.tab1.setLayout(self.infolayout)
        self.dyn_canv=FigureCanvas(Figure(figsize=(5,5)))
        self.ax_dyn=self.dyn_canv.figure.subplots()
        self.timer=self.dyn_canv.new_timer(interval=100)
        self.timer.add_callback(self.trace,self.ax_dyn)
        self.timer.start()
        self.courbelayout=QGridLayout()
        self.courbelayout.addWidget(self.dyn_canv)
        self.tab2.setLayout(self.courbelayout)
    #la fonction trace (ajout valeur aléatoire pour le tracer)
    def trace(self,ax):
        ax.figure.canvas.draw()
        self.Index +=1
        self.val = self.thermo.value#random.random()
        self.tabval.append(self.val)
        ax.plot(np.asarray(self.tabval))
        #apposons notre layout principal à notre fenêtre
        self.base.setLayout(self.mainLayout)
        self.base.show()
    #ajout des getters 
    def get_temp(self):
        tt = psutil.sensors_temperatures()
        temp_list = []
        for n,i in tt.items():
            for ii in i:
                temp_list.append(ii.current)
        return temp_list
    def affiche(self):
        self.setPval(int(psutil.cpu_percent(0.5)))
        self.setHval(int(psutil.virtual_memory().percent))
        self.setRSSI(int(psutil.swap_memory().percent))
        temp=self.get_temp()
        self.setTemp(int(temp[0]))#temperature moyenne des CPU
#Interface terminée
#créons l'application elle même
if __name__ == "__main__":
    app = QApplication(sys.argv)
    IHM = Monitoring()
    timer=QTimer()
    timer.timeout.connect(IHM.affiche)
    timer.start(100) #uptdate toute les millsecondes
    app.exec_()












        


