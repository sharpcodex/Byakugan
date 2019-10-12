# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main_window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Mainindow(object):
    def setupUi(self, Mainindow):
        Mainindow.setObjectName("Mainindow")
        Mainindow.resize(802, 601)
        self.centralwidget = QtWidgets.QWidget(Mainindow)
        self.centralwidget.setObjectName("centralwidget")
        Mainindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Mainindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 802, 21))
        self.menubar.setObjectName("menubar")
        Mainindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Mainindow)
        self.statusbar.setObjectName("statusbar")
        Mainindow.setStatusBar(self.statusbar)

        self.retranslateUi(Mainindow)
        QtCore.QMetaObject.connectSlotsByName(Mainindow)

    def retranslateUi(self, Mainindow):
        _translate = QtCore.QCoreApplication.translate
        Mainindow.setWindowTitle(_translate("Mainindow", "MainWindow"))

