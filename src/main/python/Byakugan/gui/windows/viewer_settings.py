from qtpy.QtWidgets import QDialog

from gui.windows.ui.ui_viewer_settings import Ui_ViewerSettings


class ViewerSettingsDialog(QDialog, Ui_ViewerSettings):
    def __init__(self, *args, **kwargs):
        super(ViewerSettingsDialog, self).__init__(*args, **kwargs)
        self.setupUi(self)
