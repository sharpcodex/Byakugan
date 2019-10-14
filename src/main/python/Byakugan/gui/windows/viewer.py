from qtpy.QtCore import Qt
from qtpy.QtWidgets import QMainWindow, QToolBar

from gui.windows.shared.window_actions import WindowActions
from gui.windows.ui.ui_viewer import Ui_ViewerWindow


class ViewerWindow(QMainWindow, Ui_ViewerWindow):
    def __init__(self, app_manager, theme_manager, *args, **kwargs):
        # class init
        super(ViewerWindow, self).__init__(*args, **kwargs)
        self.app = app_manager
        self.theme = theme_manager
        # Setup Ui
        self.setupUi(self)
        self.actions = WindowActions(self.theme)
        self.toolbar = QToolBar('toolbar')
        self.addToolBar(self.toolbar)
        # Setup Ui
        self.setWindowTitle(self.app.config.app_name)
        self.setWindowIcon(self.theme.window_icon)
        self.toolbar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        # Setup actions
        self.actions.full_screen_action.triggered.connect(self.full_screen_action_triggered)
        self.actions.exit_action.triggered.connect(self.app.quit)
        # Setup toolbar
        self.toolbar.addAction(self.actions.full_screen_action)
        self.toolbar.addAction(self.actions.exit_action)

    # Actions
    @staticmethod
    def full_screen_action_triggered():
        print("Show in full screen mode")

    # Helpers
    def bar_log(self, msg):
        self.statusBar().showMessage(msg)
