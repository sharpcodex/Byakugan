from qtpy.QtCore import Qt
from qtpy.QtWidgets import QMainWindow, QToolBar, QDesktopWidget, QSizePolicy

from gui.windows.shared.window_actions import WindowActions
from gui.windows.ui.ui_viewer import Ui_ViewerWindow


class ViewerWindow(QMainWindow, Ui_ViewerWindow):
    def __init__(self, app_manager, images_list, *args, **kwargs):
        # class init
        super(ViewerWindow, self).__init__(*args, **kwargs)
        self.app = app_manager
        self.images_list = images_list
        # Setup Ui
        self.setupUi(self)
        self.actions = WindowActions(self.app)
        self.toolbar = QToolBar('toolbar')
        self.addToolBar(self.toolbar)
        # Setup Ui
        self.setWindowTitle(self.app.app_name)
        self.setWindowIcon(self.app.ui.window_icon)
        # self.toolbar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.resize(self.app.ui.window_width, self.app.ui.window_height)
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.label.setAlignment(Qt.AlignCenter)
        # self.label.setScaledContents(True)

        # Setup actions
        self.actions.previous.triggered.connect(self.app.quit)
        self.actions.next.triggered.connect(self.app.quit)
        self.actions.fullscreen.triggered.connect(self.full_screen_action_triggered)
        self.actions.slideshow.triggered.connect(self.full_screen_action_triggered)
        # --
        self.actions.rotate.triggered.connect(self.full_screen_action_triggered)
        self.actions.flip.triggered.connect(self.full_screen_action_triggered)
        # --
        self.actions.reload.triggered.connect(self.app.quit)
        self.actions.exit.triggered.connect(self.app.quit)
        # Setup toolbar
        self.toolbar.addAction(self.actions.previous)
        self.toolbar.addAction(self.actions.next)
        self.toolbar.addAction(self.actions.fullscreen)
        self.toolbar.addAction(self.actions.slideshow)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.actions.rotate)
        self.toolbar.addAction(self.actions.flip)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.actions.reload)
        self.toolbar.addAction(self.actions.exit)
        # Show first image
        self.show_image(self.images_list.get_next())
        qt_rectangle = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        qt_rectangle.moveCenter(center_point)
        self.move(qt_rectangle.topLeft())

    # Actions
    @staticmethod
    def full_screen_action_triggered():
        print("Show in full screen mode")

    def show_image(self, vimage):
        pixmap = vimage.pixmap
        target_width = self.width() if pixmap.width() > self.width() else pixmap.width()
        target_height = self.height() if pixmap.height() > self.height() else pixmap.height()
        pixmap = pixmap.scaled(target_width, target_height, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.label.setPixmap(pixmap)

    # Helpers
    def bar_log(self, msg):
        self.statusBar().showMessage(msg)
