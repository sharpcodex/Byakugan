from qtpy.QtCore import Qt, QPoint
from qtpy.QtWidgets import QMainWindow, QToolBar, QDesktopWidget

from gui.windows.shared.window_actions import WindowActions
from gui.windows.ui.ui_viewer import Ui_ViewerWindow


class ViewerWindow(QMainWindow, Ui_ViewerWindow):
    def __init__(self, app_manager, images_list, *args, **kwargs):
        # class init
        super(ViewerWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.app = app_manager
        self.images_list = images_list
        self.old_pos = self.pos()

        # Setup: window
        self.setWindowTitle(self.app.app_name)
        self.setWindowIcon(self.app.ui.window_icon)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.resize(self.app.ui.window_width, self.app.ui.window_height)
        self.centralwidget.layout().setContentsMargins(0, 0, 0, 0)
        self.label.mouseDoubleClickEvent = self.label_double_click_event
        # Setup: actions
        self.actions = WindowActions(self.app)

        self.actions.previous.triggered.connect(self.previous)
        self.actions.next.triggered.connect(self.next)
        self.actions.zoom_in.triggered.connect(self.zoomin)
        self.actions.zoom_out.triggered.connect(self.zoomout)
        self.actions.rotate.triggered.connect(self.rotate)
        self.actions.flip.triggered.connect(self.flip)
        self.actions.scale_w.triggered.connect(self.scale_w)
        self.actions.scale_h.triggered.connect(self.scale_h)
        self.actions.scale.triggered.connect(self.scale)
        self.actions.fullscreen.triggered.connect(self.fullscreen)
        self.actions.slideshow.triggered.connect(self.slideshow)
        self.actions.info.triggered.connect(self.info)
        self.actions.save_as.triggered.connect(self.save_as)
        self.actions.print.triggered.connect(self.print)
        self.actions.delete_item.triggered.connect(self.delete_item)
        self.actions.settings.triggered.connect(self.settings)
        self.actions.minimize.triggered.connect(self.minimize)
        self.actions.maximize.triggered.connect(self.maximize)
        self.actions.exit.triggered.connect(self.app.quit)

        # Setup: toolbar
        self.toolbar = QToolBar('toolbar')
        self.toolbar.setMovable(False)
        self.toolbar.setContextMenuPolicy(Qt.NoContextMenu)
        self.toolbar.setContextMenuPolicy(Qt.PreventContextMenu)
        self.setContextMenuPolicy(Qt.NoContextMenu)

        self.addToolBar(self.toolbar)

        self.toolbar.addAction(self.actions.previous)
        self.toolbar.addAction(self.actions.next)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.actions.zoom_in)
        self.toolbar.addAction(self.actions.zoom_out)
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
        self.toolbar.addWidget(self.actions.separator)
        self.toolbar.addAction(self.actions.minimize)
        self.toolbar.addAction(self.actions.maximize)
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
        if self.isFullScreen():
            self.showNormal()
        else:
            self.showFullScreen()

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

    def minimize(self):
        self.showMinimized()

    def maximize(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    def show_image(self, vimage):
        pixmap = vimage.pixmap
        target_width = self.width() if pixmap.width() > self.width() else pixmap.width()
        target_height = self.height() if pixmap.height() > self.height() else pixmap.height()
        pixmap = pixmap.scaled(target_width, target_height, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.label.setPixmap(pixmap)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def label_double_click_event(self, event):
        pass

    def mouseDoubleClickEvent(self, event):
        self.maximize()

    def mousePressEvent(self, event):
        self.old_pos = event.globalPos()

    def mouseReleaseEvent(self, event):
        self.setWindowOpacity(1)

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.old_pos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.old_pos = event.globalPos()
        self.setWindowOpacity(0.5)

    # Helpers
    def bar_log(self, msg):
        self.statusBar().showMessage(msg)
