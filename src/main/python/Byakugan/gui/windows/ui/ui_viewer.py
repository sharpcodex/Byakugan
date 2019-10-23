# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\workspace\Byakugan\Byakugan\src\main\python\Byakugan\gui\windows\ui\ui_viewer.ui'
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
        self.centralwidget_gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.centralwidget_gridLayout.setObjectName("centralwidget_gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 780, 539))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea_gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.scrollArea_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_gridLayout.setSpacing(0)
        self.scrollArea_gridLayout.setObjectName("scrollArea_gridLayout")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.scrollArea_gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.centralwidget_gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
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

