# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\WorkSpace\myGithub\Byakugan\Byakugan\src\main\python\Byakugan\gui\windows\ui\ui_viewer.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ViewerWindow(object):
    def setupUi(self, ViewerWindow):
        ViewerWindow.setObjectName("ViewerWindow")
        ViewerWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(ViewerWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        ViewerWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ViewerWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        ViewerWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ViewerWindow)
        self.statusbar.setSizeGripEnabled(True)
        self.statusbar.setObjectName("statusbar")
        ViewerWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ViewerWindow)
        QtCore.QMetaObject.connectSlotsByName(ViewerWindow)

    def retranslateUi(self, ViewerWindow):
        _translate = QtCore.QCoreApplication.translate
        ViewerWindow.setWindowTitle(_translate("ViewerWindow", "MainWindow"))

