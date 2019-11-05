from qtpy.QtWidgets import QDialog, QDialogButtonBox
from qtpy.QtCore import Qt
from gui.windows.ui.ui_settings import Ui_SettingsDialog
from app.settings_manager import *


class SettingsDialog(QDialog, Ui_SettingsDialog):
    def __init__(self, app_manager, *args, **kwargs):
        super(SettingsDialog, self).__init__(*args, **kwargs)
        self.setupUi(self)

        # Init self
        self.app = app_manager
        self.current_settings = self.app.settings.get_all()

        # Init events
        self.buttonBox.clicked.connect(self.handleButtonClick)

        # Load current Settings
        self.load_settings()

    def handleButtonClick(self, button):
        btn = self.buttonBox.standardButton(button)
        if btn == QDialogButtonBox.Apply:
            self.save_settings()
        elif btn == QDialogButtonBox.Ok:
            self.save_settings()
            self.close()
        else:
            self.close()

    def save_settings(self):
        self.app.settings.set_all({
            # Look and feel
            APP_THEME: self.app_theme_combo.currentText(),
            APP_COLOR: self.app_color_combo.currentText(),
            M_SHOW_STATUS_BAR: self.m_show_status_bar_checkbox.isChecked(),
            M_SAVE_WINDOW_GEOMETRY: self.m_save_window_geometry_checkbox.isChecked(),
            V_SHOW_STATUS_BAR: self.v_show_status_bar_checkbox.isChecked(),
            V_SAVE_WINDOW_GEOMETRY: self.v_save_window_geometry_checkbox.isChecked(),
            E_SHOW_STATUS_BAR: self.e_show_status_bar_checkbox.isChecked(),
            E_SAVE_WINDOW_GEOMETRY: self.e_save_window_geometry_checkbox.isChecked(),
        })

    def load_settings(self):
        d = self.current_settings

        # Look and feel
        index = self.app_theme_combo.findText(d[APP_THEME], Qt.MatchFixedString)
        if index >= 0:
            self.app_theme_combo.setCurrentIndex(index)

        index = self.app_color_combo.findText(d[APP_COLOR], Qt.MatchFixedString)
        if index >= 0:
            self.app_color_combo.setCurrentIndex(index)

        self.m_show_status_bar_checkbox.setChecked(self.app.settings.get(M_SHOW_STATUS_BAR))
        self.m_save_window_geometry_checkbox.setChecked(self.app.settings.get(M_SAVE_WINDOW_GEOMETRY))
        self.v_show_status_bar_checkbox.setChecked(self.app.settings.get(V_SHOW_STATUS_BAR))
        self.v_save_window_geometry_checkbox.setChecked(self.app.settings.get(V_SAVE_WINDOW_GEOMETRY))
        self.e_show_status_bar_checkbox.setChecked(self.app.settings.get(E_SHOW_STATUS_BAR))
        self.e_save_window_geometry_checkbox.setChecked(self.app.settings.get(E_SAVE_WINDOW_GEOMETRY))
