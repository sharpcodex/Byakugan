# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\workspace\Byakugan\Byakugan\src\main\python\Byakugan\gui\windows\ui\ui_viewer_help.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ViewerHelpDialog(object):
    def setupUi(self, ViewerHelpDialog):
        ViewerHelpDialog.setObjectName("ViewerHelpDialog")
        ViewerHelpDialog.resize(315, 592)
        ViewerHelpDialog.setModal(True)
        self.gridLayout = QtWidgets.QGridLayout(ViewerHelpDialog)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(ViewerHelpDialog)
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setTabKeyNavigation(False)
        self.tableWidget.setProperty("showDropIndicator", False)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setCornerButtonEnabled(False)
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)

        self.retranslateUi(ViewerHelpDialog)
        QtCore.QMetaObject.connectSlotsByName(ViewerHelpDialog)

    def retranslateUi(self, ViewerHelpDialog):
        _translate = QtCore.QCoreApplication.translate
        ViewerHelpDialog.setWindowTitle(_translate("ViewerHelpDialog", "Shortcuts List"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ViewerHelpDialog", "Action"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ViewerHelpDialog", "Shortcut"))

