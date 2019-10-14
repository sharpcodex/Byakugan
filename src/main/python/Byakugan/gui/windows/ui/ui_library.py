# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\workspace\Byakugan\Byakugan\src\main\python\Byakugan\windows\ui\ui_library.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LibraryManagerWindow(object):
    def setupUi(self, LibraryManagerWindow):
        LibraryManagerWindow.setObjectName("LibraryManagerWindow")
        LibraryManagerWindow.resize(555, 344)
        self.gridLayout = QtWidgets.QGridLayout(LibraryManagerWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.list = QtWidgets.QListWidget(LibraryManagerWindow)
        self.list.setObjectName("list")
        self.horizontalLayout.addWidget(self.list)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.addBtn = QtWidgets.QPushButton(LibraryManagerWindow)
        self.addBtn.setObjectName("addBtn")
        self.verticalLayout.addWidget(self.addBtn)
        self.removeBtn = QtWidgets.QPushButton(LibraryManagerWindow)
        self.removeBtn.setObjectName("removeBtn")
        self.verticalLayout.addWidget(self.removeBtn)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(LibraryManagerWindow)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.retranslateUi(LibraryManagerWindow)
        self.buttonBox.accepted.connect(LibraryManagerWindow.accept)
        self.buttonBox.rejected.connect(LibraryManagerWindow.reject)
        QtCore.QMetaObject.connectSlotsByName(LibraryManagerWindow)

    def retranslateUi(self, LibraryManagerWindow):
        _translate = QtCore.QCoreApplication.translate
        LibraryManagerWindow.setWindowTitle(_translate("LibraryManagerWindow", "Dialog"))
        self.addBtn.setText(_translate("LibraryManagerWindow", "Add"))
        self.removeBtn.setText(_translate("LibraryManagerWindow", "Remove"))

