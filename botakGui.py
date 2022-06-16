from form import Ui_Widget
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt,QTimer,QTime,QDate
from PyQt5.uic import loadUiType
import data_collection
import botak
import os
import sys

class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()
        
    def run(self):
        botak.main()
   
StartExe = MainThread()

class Gui_Start(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.gui = Ui_Widget()
        self.gui.setupUi(self)
        
        self.gui.pushButton.clicked.connect(self.startTask)
        self.gui.pushButton_3.clicked.connect(self.face)
        self.gui.pushButton_2.clicked.connect(self.path)
        
    def startTask(self):
        self.gui.label3 = QtGui.QMovie("../../Downloads/circle-unscreen.gif")
        self.gui.label_3.setMovie(self.gui.label3)
        self.gui.label3.start()
        StartExe.start()
        
    def face(self):
        data_collection.main()
    
    def path(self):
        os.startfile('path.txt')

GuiApp = QApplication(sys.argv)
botakGUI = Gui_Start()
botakGUI.show()
sys.exit(GuiApp.exec_())