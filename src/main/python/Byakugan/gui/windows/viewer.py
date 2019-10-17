from qtpy.QtCore import Qt, QPoint
from qtpy.QtWidgets import QMainWindow, QToolBar

from gui.windows.shared.window_actions import WindowActions
from gui.windows.ui.ui_viewer import Ui_ViewerWindow


class ViewerWindow(QMainWindow, Ui_ViewerWindow):
    def __init__(self, app_manager, images_list, *args, **kwargs):
        # class init
        super(ViewerWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.app = app_manager
        self.images_list = images_list

        # Setup: window
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowTitle(self.app.app_name)
        self.setWindowIcon(self.app.ui.window_icon)
        self.centralwidget.layout().setContentsMargins(0, 0, 0, 0)

        # Setup self
        self.old_pos = self.pos()
        self.window_moving = False

        # Setup: events
        self.label.mouseDoubleClickEvent = self.label_double_click_event

        # Setup: actions
        self.actions = WindowActions(self.app)
        self.actions.previous.triggered.connect(self.previous_action)
        self.actions.next.triggered.connect(self.next_action)
        self.actions.zoom_in.triggered.connect(self.zoom_in_action)
        self.actions.zoom_out.triggered.connect(self.zoom_out_action)
        self.actions.rotate.triggered.connect(self.rotate_action)
        self.actions.flip.triggered.connect(self.flip_action)
        self.actions.scale_w.triggered.connect(self.scale_w_action)
        self.actions.scale_h.triggered.connect(self.scale_h_action)
        self.actions.scale.triggered.connect(self.scale_action)
        self.actions.info.triggered.connect(self.info_action)
        self.actions.save_as.triggered.connect(self.save_as_action)
        self.actions.print.triggered.connect(self.print_action)
        self.actions.delete_item.triggered.connect(self.delete_action)
        self.actions.settings.triggered.connect(self.settings_action)
        self.actions.slideshow.triggered.connect(self.slideshow_action)
        self.actions.minimize.triggered.connect(self.minimize_action)
        self.actions.maximize.triggered.connect(self.maximize_action)
        self.actions.exit.triggered.connect(self.exit_action)

        # Setup: toolbar
        self.toolbar = QToolBar('toolbar')
        self.toolbar.setMovable(False)
        self.toolbar.setContextMenuPolicy(Qt.NoContextMenu)
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
        self.toolbar.addWidget(self.actions.separator)
        self.toolbar.addAction(self.actions.slideshow)
        self.toolbar.addAction(self.actions.minimize)
        self.toolbar.addAction(self.actions.maximize)
        self.toolbar.addAction(self.actions.exit)

        # Setup: context menu
        self.label.addAction(self.actions.previous)
        self.label.addAction(self.actions.next)
        self.label.addAction(self.actions.zoom_in)
        self.label.addAction(self.actions.zoom_out)
        self.label.addAction(self.actions.rotate)
        self.label.addAction(self.actions.flip)
        self.label.addAction(self.actions.scale_w)
        self.label.addAction(self.actions.scale_h)
        self.label.addAction(self.actions.scale)
        self.label.addAction(self.actions.info)
        self.label.addAction(self.actions.save_as)
        self.label.addAction(self.actions.print)
        self.label.addAction(self.actions.delete_item)
        self.label.addAction(self.actions.settings)
        self.label.addAction(self.actions.slideshow)
        self.label.addAction(self.actions.exit)

        # Show first image
        self.show_image(self.images_list.get_next())

        # Restore last window state
        self._restoreGeometry()
        self._startup()

    # Actions

    def previous_action(self):
        print("previous")

    def next_action(self):
        print("next")

    def zoom_in_action(self):
        print("zoomin")

    def zoom_out_action(self):
        print("zoomout")

    def rotate_action(self):
        print("rotate")

    def flip_action(self):
        print("flip")

    def scale_w_action(self):
        print("scale_w")

    def scale_h_action(self):
        print("scale_h")

    def scale_action(self):
        print("scale")

    def info_action(self):
        print("info")

    def save_as_action(self):
        print("save_as")

    def print_action(self):
        print("print")

    def delete_action(self):
        print("delete")

    def settings_action(self):
        print("settings")

    def slideshow_action(self):
        if self.isFullScreen():
            self._showNormal()
        else:
            self._showFullScreen()

    def minimize_action(self):
        self.showMinimized()

    def maximize_action(self):
        if self.isMaximized():
            self._showNormal()
        else:
            self._showMaximized()

    def exit_action(self):
        if self.isFullScreen():
            self._showNormal()
        self._saveGeometry()
        self.close()
        self.app.quit()

    # Events

    def label_double_click_event(self, event):
        pass

    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.maximize_action()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.old_pos = event.globalPos()
            self.window_moving = True

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.setWindowOpacity(1)
            self.window_moving = False

    def mouseMoveEvent(self, event):
        if self.window_moving and not self.isMaximized() and not self.isFullScreen():
            delta = QPoint(event.globalPos() - self.old_pos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.old_pos = event.globalPos()
            self.setWindowOpacity(0.5)

    # Helpers

    def show_image(self, vimage):
        pixmap = vimage.pixmap
        target_width = self.width() if pixmap.width() > self.width() else pixmap.width()
        target_height = self.height() if pixmap.height() > self.height() else pixmap.height()
        pixmap = pixmap.scaled(target_width, target_height, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.label.setPixmap(pixmap)

    def bar_log(self, msg):
        self.statusBar().showMessage(msg)

    def _showNormal(self):
        self.showNormal()
        self.actions.maximize.setIcon(self.app.ui.maximize_icon)
        self.actions.minimize.setVisible(True)
        self.actions.maximize.setVisible(True)

    def _showMaximized(self):
        self.showMaximized()
        self.actions.maximize.setIcon(self.app.ui.restore_icon)

    def _showFullScreen(self):
        self.showFullScreen()
        self.actions.minimize.setVisible(False)
        self.actions.maximize.setVisible(False)

    def _saveGeometry(self):
        geometry = self.saveGeometry()
        self.app.settings.set('viewer_window_geometry', geometry)

    def _restoreGeometry(self):
        show_status_bar = self.app.settings.get('vui_show_status_bar', False, bool)
        load_geometry = self.app.settings.get('vui_save_window_geometry', False, bool)

        self.statusbar.setVisible(show_status_bar)

        if load_geometry:
            last_geometry = self.app.settings.get_value('viewer_window_geometry', '')
            try:
                self.restoreGeometry(last_geometry)
                if self.isMaximized():
                    self._showMaximized()
                else:
                    self._showNormal()
            except Exception:
                self._center_window()
        else:
            self._center_window()

    def _center_window(self):
        self.resize(self.app.ui.best_window_width, self.app.ui.best_window_height)
        frame_geometry = self.frameGeometry()
        frame_geometry.moveCenter(self.app.ui.screen_center)
        self.move(frame_geometry.topLeft())

    def _startup(self):
        print(self.app.app_name)
