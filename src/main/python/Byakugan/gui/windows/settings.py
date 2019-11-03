from qtpy.QtWidgets import QDialog

from gui.windows.ui.ui_settings import Ui_SettingsDialog


class SettingsDialog(QDialog, Ui_SettingsDialog):
    def __init__(self, *args, **kwargs):
        super(SettingsDialog, self).__init__(*args, **kwargs)
        self.setupUi(self)
