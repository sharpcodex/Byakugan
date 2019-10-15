from qtpy.QtCore import Qt
from qtpy.QtWidgets import QMainWindow, QToolBar

from gui.windows.shared.window_actions import WindowActions
from gui.windows.ui.ui_main import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, app_manager, *args, **kwargs):
        # class init
        super(MainWindow, self).__init__(*args, **kwargs)
        self.app = app_manager
        # Setup Ui
        self.setupUi(self)
        self.actions = WindowActions(self.app)
        self.toolbar = QToolBar('toolbar')
        self.addToolBar(self.toolbar)
        # Setup Ui
        self.setWindowTitle(self.app.app_name)
        self.setWindowIcon(self.app.ui.window_icon)
        self.toolbar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        # Setup actions
        self.actions.fullscreen.triggered.connect(self.full_screen_action_triggered)
        self.actions.exit.triggered.connect(self.app.quit)
        # Setup menus
        self.menu_File.addAction(self.actions.exit)
        self.menu_View.addAction(self.actions.fullscreen)
        # Setup toolbar
        self.toolbar.addAction(self.actions.fullscreen)
        self.toolbar.addAction(self.actions.exit)

    # Actions
    @staticmethod
    def full_screen_action_triggered():
        print("Show in full screen mode")

    # Helpers
    def bar_log(self, msg):
        self.statusBar().showMessage(msg)
