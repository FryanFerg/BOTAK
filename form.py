# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(800, 600)
        self.label = QtWidgets.QLabel(Widget)
        self.label.setGeometry(QtCore.QRect(-80, -80, 921, 701))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../Downloads/solid-color-image(1).png"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Widget)
        self.label_2.setGeometry(QtCore.QRect(140, 130, 49, 16))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../../Downloads/circle-unscreen.gif"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Widget)
        self.label_3.setGeometry(QtCore.QRect(140, 170, 381, 261))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../../Downloads/circle-unscreen.gif"))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Widget)
        self.pushButton.setGeometry(QtCore.QRect(290, 270, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color:#000000;\n"
"color: rgb(255, 255, 255);\n"
"border-radius:none;")
        self.pushButton.setCheckable(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Widget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 20, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("border-radius:none;\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Widget)
        self.pushButton_3.setGeometry(QtCore.QRect(140, 20, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("border-radius:none;\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButton_3.setCheckable(False)
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.pushButton.setText(_translate("Widget", "START"))
        self.pushButton_2.setText(_translate("Widget", "Path"))
        self.pushButton_3.setText(_translate("Widget", "Face"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())
