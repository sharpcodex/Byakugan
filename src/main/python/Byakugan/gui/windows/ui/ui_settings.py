# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\workspace\Byakugan\Byakugan\src\main\python\Byakugan\gui\windows\ui\ui_settings.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        SettingsDialog.setObjectName("SettingsDialog")
        SettingsDialog.resize(529, 333)
        self.gridLayout = QtWidgets.QGridLayout(SettingsDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(SettingsDialog)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(484, 27, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 4, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.app_theme_combo = QtWidgets.QComboBox(self.tab)
        self.app_theme_combo.setMinimumSize(QtCore.QSize(150, 0))
        self.app_theme_combo.setObjectName("app_theme_combo")
        self.app_theme_combo.addItem("")
        self.app_theme_combo.addItem("")
        self.app_theme_combo.addItem("")
        self.app_theme_combo.addItem("")
        self.horizontalLayout.addWidget(self.app_theme_combo)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.app_color_combo = QtWidgets.QComboBox(self.tab)
        self.app_color_combo.setMinimumSize(QtCore.QSize(150, 0))
        self.app_color_combo.setObjectName("app_color_combo")
        self.app_color_combo.addItem("")
        self.app_color_combo.addItem("")
        self.app_color_combo.addItem("")
        self.app_color_combo.addItem("")
        self.app_color_combo.addItem("")
        self.horizontalLayout_2.addWidget(self.app_color_combo)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.m_show_status_bar_checkbox = QtWidgets.QCheckBox(self.groupBox_3)
        self.m_show_status_bar_checkbox.setObjectName("m_show_status_bar_checkbox")
        self.verticalLayout_5.addWidget(self.m_show_status_bar_checkbox)
        self.m_save_window_geometry_checkbox = QtWidgets.QCheckBox(self.groupBox_3)
        self.m_save_window_geometry_checkbox.setObjectName("m_save_window_geometry_checkbox")
        self.verticalLayout_5.addWidget(self.m_save_window_geometry_checkbox)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.v_show_status_bar_checkbox = QtWidgets.QCheckBox(self.groupBox_2)
        self.v_show_status_bar_checkbox.setObjectName("v_show_status_bar_checkbox")
        self.verticalLayout_4.addWidget(self.v_show_status_bar_checkbox)
        self.v_save_window_geometry_checkbox = QtWidgets.QCheckBox(self.groupBox_2)
        self.v_save_window_geometry_checkbox.setObjectName("v_save_window_geometry_checkbox")
        self.verticalLayout_4.addWidget(self.v_save_window_geometry_checkbox)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.e_show_status_bar_checkbox = QtWidgets.QCheckBox(self.groupBox)
        self.e_show_status_bar_checkbox.setObjectName("e_show_status_bar_checkbox")
        self.verticalLayout_3.addWidget(self.e_show_status_bar_checkbox)
        self.e_save_window_geometry_checkbox = QtWidgets.QCheckBox(self.groupBox)
        self.e_save_window_geometry_checkbox.setObjectName("e_save_window_geometry_checkbox")
        self.verticalLayout_3.addWidget(self.e_save_window_geometry_checkbox)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(SettingsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Apply|QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 1, 1, 1)

        self.retranslateUi(SettingsDialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(SettingsDialog)

    def retranslateUi(self, SettingsDialog):
        _translate = QtCore.QCoreApplication.translate
        SettingsDialog.setWindowTitle(_translate("SettingsDialog", "Dialog"))
        self.label.setText(_translate("SettingsDialog", "Theme"))
        self.app_theme_combo.setItemText(0, _translate("SettingsDialog", "Dark"))
        self.app_theme_combo.setItemText(1, _translate("SettingsDialog", "Light"))
        self.app_theme_combo.setItemText(2, _translate("SettingsDialog", "Compact"))
        self.app_theme_combo.setItemText(3, _translate("SettingsDialog", "Classic"))
        self.label_2.setText(_translate("SettingsDialog", "Color"))
        self.app_color_combo.setItemText(0, _translate("SettingsDialog", "Red"))
        self.app_color_combo.setItemText(1, _translate("SettingsDialog", "Green"))
        self.app_color_combo.setItemText(2, _translate("SettingsDialog", "Yellow"))
        self.app_color_combo.setItemText(3, _translate("SettingsDialog", "Black"))
        self.app_color_combo.setItemText(4, _translate("SettingsDialog", "White"))
        self.groupBox_3.setTitle(_translate("SettingsDialog", "Manager"))
        self.m_show_status_bar_checkbox.setText(_translate("SettingsDialog", "show status bar"))
        self.m_save_window_geometry_checkbox.setText(_translate("SettingsDialog", "save window geometry"))
        self.groupBox_2.setTitle(_translate("SettingsDialog", "Viewer"))
        self.v_show_status_bar_checkbox.setText(_translate("SettingsDialog", "show status bar"))
        self.v_save_window_geometry_checkbox.setText(_translate("SettingsDialog", "save window geometry"))
        self.groupBox.setTitle(_translate("SettingsDialog", "Editor"))
        self.e_show_status_bar_checkbox.setText(_translate("SettingsDialog", "show status bar"))
        self.e_save_window_geometry_checkbox.setText(_translate("SettingsDialog", "save window geometry"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("SettingsDialog", "Look and Feel"))

