from qtpy.QtWidgets import QDialog, QDialogButtonBox
from qtpy.QtCore import Qt
from gui.windows.ui.ui_settings import Ui_SettingsDialog


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
            'app_theme': self.app_theme_combo.currentText(),
            'app_color': self.app_color_combo.currentText(),
            'm_show_status_bar': self.m_show_status_bar_checkbox.isChecked(),
            'm_save_window_geometry': self.m_save_window_geometry_checkbox.isChecked(),
            'v_show_status_bar': self.v_show_status_bar_checkbox.isChecked(),
            'v_save_window_geometry': self.v_save_window_geometry_checkbox.isChecked(),
            'e_show_status_bar': self.e_show_status_bar_checkbox.isChecked(),
            'e_save_window_geometry': self.e_save_window_geometry_checkbox.isChecked(),
        })

    def load_settings(self):
        d = self.current_settings
        print(d)
        # Look and feel
        index = self.app_theme_combo.findText(d['app_theme'], Qt.MatchFixedString)
        if index >= 0:
            self.app_theme_combo.setCurrentIndex(index)

        index = self.app_color_combo.findText(d['app_color'], Qt.MatchFixedString)
        if index >= 0:
            self.app_color_combo.setCurrentIndex(index)

        self.m_show_status_bar_checkbox.setChecked(self._read_bool('m_show_status_bar'))
        self.m_save_window_geometry_checkbox.setChecked(self._read_bool('m_save_window_geometry'))
        self.v_show_status_bar_checkbox.setChecked(self._read_bool('v_show_status_bar'))
        self.v_save_window_geometry_checkbox.setChecked(self._read_bool('v_save_window_geometry'))
        self.e_show_status_bar_checkbox.setChecked(self._read_bool('e_show_status_bar'))
        self.e_save_window_geometry_checkbox.setChecked(self._read_bool('e_save_window_geometry'))

    def _read_bool(self, key):
        return self.app.settings.read(key, value_type=bool)
