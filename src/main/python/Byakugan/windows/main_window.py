from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QToolBar, QAction
from PyQt5.uic import loadUi
import qtawesome as qta
from fbs_runtime.application_context import cached_property


class MainWindow(QMainWindow):
    def __init__(self, ctx, *args, **kwargs):
        # class init
        self.ctx = ctx
        super(MainWindow, self).__init__(*args, **kwargs)
        # Load Ui
        loadUi(self.ui_file, self)
        self.installEventFilter(QWindowEventFilter(self))
        # Window setup
        self.setWindowIcon(self.window_icon)
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
        exit_action.triggered.connect(self.exit_action_triggered)
        return exit_action

    @staticmethod
    def exit_action_triggered():
        QtCore.QCoreApplication.instance().quit()

    @cached_property
    def full_screen_action(self):
        full_screen_action = QAction(qta.icon('fa5s.expand'), "Full Screen", self)
        full_screen_action.setToolTip("Show in full screen mode")
        full_screen_action.setStatusTip("Show in full screen mode")
        full_screen_action.triggered.connect(self.full_screen_action_triggered)
        return full_screen_action

    @staticmethod
    def full_screen_action_triggered():
        print("Show in full screen mode")

    # Helpers
    @staticmethod
    def on_window_activation():
        print("on_window_activation")

    @staticmethod
    def on_window_deactivation():
        print("on_window_deactivation")

    def bar_log(self, msg):
        self.statusBar().showMessage(msg)

    @cached_property
    def ui_file(self):
        return str(self.ctx.get_resource('ui/ui_main_window.ui'))

    @cached_property
    def window_icon(self):
        return QIcon(self.ctx.get_resource('images/main.png'))


class QWindowEventFilter(QtCore.QObject):
    def __init__(self, parent=None):
        QtCore.QObject.__init__(self, parent)

    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.ActivationChange:
            if self.parent().isActiveWindow():
                self.parent().on_window_activation()
            else:
                self.parent().on_window_deactivation()
        return QtCore.QObject.eventFilter(self, obj, event)
