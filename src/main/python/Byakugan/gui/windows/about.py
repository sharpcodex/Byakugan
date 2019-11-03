from qtpy.QtWidgets import QDialog

from gui.windows.ui.ui_about import Ui_AboutDialog


class AboutDialog(QDialog, Ui_AboutDialog):
    def __init__(self, *args, **kwargs):
        super(AboutDialog, self).__init__(*args, **kwargs)
        self.setupUi(self)
