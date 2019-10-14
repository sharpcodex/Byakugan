from fbs_runtime.application_context import cached_property
from qtpy.QtCore import Qt
from qtpy.QtWidgets import QMainWindow, QToolBar, QAction
import qtawesome as qta

from gui.windows.ui.ui_main import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, app_manager, theme_manager, *args, **kwargs):
        # class init
        self.app = app_manager
        self.theme = theme_manager
        super(MainWindow, self).__init__(*args, **kwargs)
        # Load Ui
        self.setupUi(self)
        # Setup window
        self.setWindowTitle(self.app.config.app_name)
        self.setWindowIcon(self.theme.window_icon)
        self.toolbar = QToolBar('toolbar')
        self.toolbar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.addToolBar(self.toolbar)
        # Setup menus
        self.menu_File.addAction(self.exit_action)
        self.menu_View.addAction(self.full_screen_action)
        # Setup toolbar
        self.toolbar.addAction(self.full_screen_action)

    # Actions

    @cached_property
    def exit_action(self):
        exit_action = QAction(qta.icon('mdi.exit-to-app'), "&Exit", self)
        exit_action.setToolTip("Exit")
        exit_action.setStatusTip("Exit")
        exit_action.triggered.connect(self.app.quit)
        return exit_action

    @cached_property
    def full_screen_action(self):
        full_screen_action = QAction(self.theme.expand_icon, "Full Screen", self)
        full_screen_action.setToolTip("Show in full screen mode")
        full_screen_action.setStatusTip("Show in full screen mode")
        full_screen_action.triggered.connect(self.full_screen_action_triggered)
        return full_screen_action

    @staticmethod
    def full_screen_action_triggered():
        print("Show in full screen mode")

    # Helpers
    def bar_log(self, msg):
        self.statusBar().showMessage(msg)
