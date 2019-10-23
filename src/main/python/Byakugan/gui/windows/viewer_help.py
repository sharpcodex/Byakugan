from qtpy.QtWidgets import QDialog

from gui.windows.ui.ui_viewer_help import Ui_ViewerHelpDialog


class ViewerHelpDialog(QDialog, Ui_ViewerHelpDialog):
    def __init__(self, *args, **kwargs):
        super(ViewerHelpDialog, self).__init__(*args, **kwargs)
        self.setupUi(self)
