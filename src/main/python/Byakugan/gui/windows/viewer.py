from qtpy.QtCore import Qt
from qtpy.QtWidgets import QMainWindow, QToolBar, QSizePolicy

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
        self.setWindowTitle(self.app.app_name)
        self.setWindowIcon(self.app.ui.window_icon)
        # self.toolbar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.resize(self.app.ui.window_width, self.app.ui.window_height)
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.label.setAlignment(Qt.AlignCenter)
        # self.label.setScaledContents(True)

        # Setup actions
        self.actions.previous.triggered.connect(self.previous)
        self.actions.next.triggered.connect(self.next)
        # --
        self.actions.zoomin.triggered.connect(self.zoomin)
        self.actions.zoomout.triggered.connect(self.zoomout)
        self.actions.rotate.triggered.connect(self.rotate)
        self.actions.flip.triggered.connect(self.flip)
        self.actions.scale_w.triggered.connect(self.scale_w)
        self.actions.scale_h.triggered.connect(self.scale_h)
        self.actions.scale.triggered.connect(self.scale)
        self.actions.fullscreen.triggered.connect(self.fullscreen)
        self.actions.slideshow.triggered.connect(self.slideshow)
        self.actions.info.triggered.connect(self.info)
        # --
        self.actions.save_as.triggered.connect(self.save_as)
        self.actions.print.triggered.connect(self.print)
        self.actions.delete_item.triggered.connect(self.delete_item)
        # --
        self.actions.settings.triggered.connect(self.settings)
        self.actions.exit.triggered.connect(self.app.quit)
        # Setup toolbar
        self.toolbar.addAction(self.actions.previous)
        self.toolbar.addAction(self.actions.next)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.actions.zoomin)
        self.toolbar.addAction(self.actions.zoomout)
        self.toolbar.addAction(self.actions.rotate)
        self.toolbar.addAction(self.actions.flip)
        self.toolbar.addAction(self.actions.scale_w)
        self.toolbar.addAction(self.actions.scale_h)
        self.toolbar.addAction(self.actions.scale)
        self.toolbar.addAction(self.actions.fullscreen)
        self.toolbar.addAction(self.actions.slideshow)
        self.toolbar.addAction(self.actions.info)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.actions.save_as)
        self.toolbar.addAction(self.actions.print)
        self.toolbar.addAction(self.actions.delete_item)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.actions.settings)
        self.toolbar.addAction(self.actions.exit)
        # Show first image
        self.show_image(self.images_list.get_next())

    # Actions
    def previous(self):
        print("previous")

    def next(self):
        print("next")

    def zoomin(self):
        print("zoomin")

    def zoomout(self):
        print("zoomout")

    def rotate(self):
        print("rotate")

    def flip(self):
        print("flip")

    def scale_w(self):
        print("scale_w")

    def scale_h(self):
        print("scale_h")

    def scale(self):
        print("scale")

    def fullscreen(self):
        print("fullscreen")

    def slideshow(self):
        print("slideshow")

    def info(self):
        print("info")

    def save_as(self):
        print("save_as")

    def print(self):
        print("print")

    def delete_item(self):
        print("delete")

    def settings(self):
        print("settings")

    def show_image(self, vimage):
        pixmap = vimage.pixmap
        target_width = self.width() if pixmap.width() > self.width() else pixmap.width()
        target_height = self.height() if pixmap.height() > self.height() else pixmap.height()
        pixmap = pixmap.scaled(target_width, target_height, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.label.setPixmap(pixmap)

    # Helpers
    def bar_log(self, msg):
        self.statusBar().showMessage(msg)
