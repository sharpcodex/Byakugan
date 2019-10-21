from qtpy.QtCore import Qt, QPoint
from qtpy.QtGui import QPixmap
from qtpy.QtWidgets import QMainWindow, QToolBar

from gui.windows.shared.window_actions import WindowActions
from gui.windows.ui.ui_viewer import Ui_ViewerWindow


class ViewerWindow(QMainWindow, Ui_ViewerWindow):
    def __init__(self, app_manager, images_list, *args, **kwargs):
        super(ViewerWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        # Init self
        self.app = app_manager
        self.images_list = images_list

        self.old_pos = None
        self.window_moving = False

        self.image = next(self.images_list)
        self.image_size_policy = 'fit_auto'

        # Init UI
        self.actions = WindowActions(self.app)
        self.toolbar = QToolBar('toolbar')
        self.init_ui()

        # Init events
        self.label.mouseDoubleClickEvent = self.label_double_click_event

        # Startup
        self.startup()

    def init_ui(self):
        # Setup: window
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowTitle(self.app.app_name)
        self.setWindowIcon(self.app.ui.window_icon)
        self.centralwidget.layout().setContentsMargins(0, 0, 0, 0)

        # Setup: actions
        self.actions.previous.triggered.connect(self.previous_action)
        self.actions.next.triggered.connect(self.next_action)
        self.actions.fit_to_window.triggered.connect(self.fit_to_window)
        self.actions.fit_to_width.triggered.connect(self.fit_to_width)
        self.actions.fit_to_height.triggered.connect(self.fit_to_height)
        self.actions.show_original_size.triggered.connect(self.original_size)
        self.actions.zoom_in.triggered.connect(self.zoom_in_action)
        self.actions.zoom_out.triggered.connect(self.zoom_out_action)
        self.actions.rotate.triggered.connect(self.rotate_action)
        self.actions.flip.triggered.connect(self.flip_action)
        self.actions.info.triggered.connect(self.info_action)
        self.actions.print.triggered.connect(self.print_action)
        self.actions.delete_item.triggered.connect(self.delete_action)
        self.actions.settings.triggered.connect(self.settings_action)
        self.actions.slideshow.triggered.connect(self.slideshow_action)
        self.actions.minimize.triggered.connect(self.minimize_action)
        self.actions.maximize.triggered.connect(self.maximize_action)
        self.actions.exit.triggered.connect(self.exit_action)

        # Setup: toolbar
        self.toolbar.setMovable(False)
        self.toolbar.setContextMenuPolicy(Qt.NoContextMenu)
        self.setContextMenuPolicy(Qt.NoContextMenu)
        self.addToolBar(self.toolbar)
        self.toolbar.addAction(self.actions.previous)
        self.toolbar.addAction(self.actions.next)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.actions.fit_to_window)
        self.toolbar.addAction(self.actions.fit_to_width)
        self.toolbar.addAction(self.actions.fit_to_height)
        self.toolbar.addAction(self.actions.show_original_size)
        self.toolbar.addAction(self.actions.zoom_in)
        self.toolbar.addAction(self.actions.zoom_out)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.actions.rotate)
        self.toolbar.addAction(self.actions.flip)
        self.toolbar.addWidget(self.actions.separator)
        self.toolbar.addAction(self.actions.slideshow)
        self.toolbar.addAction(self.actions.minimize)
        self.toolbar.addAction(self.actions.maximize)
        self.toolbar.addAction(self.actions.exit)

        # Setup: context menu
        self.label.addAction(self.actions.previous)
        self.label.addAction(self.actions.next)
        self.label.addAction(self.actions.fit_to_window)
        self.label.addAction(self.actions.fit_to_width)
        self.label.addAction(self.actions.fit_to_height)
        self.label.addAction(self.actions.show_original_size)
        self.label.addAction(self.actions.zoom_in)
        self.label.addAction(self.actions.zoom_out)
        self.label.addAction(self.actions.rotate)
        self.label.addAction(self.actions.flip)
        self.label.addAction(self.actions.info)
        self.label.addAction(self.actions.print)
        self.label.addAction(self.actions.delete_item)
        self.label.addAction(self.actions.settings)
        self.label.addAction(self.actions.slideshow)
        self.label.addAction(self.actions.exit)

        # Restore last window state
        self._restore_geometry()

    def startup(self):
        # Show first image
        self.repaint_image()

    # Actions
    def previous_action(self):
        self.image = self.images_list.__prev__()
        self.repaint_image()

    def next_action(self):
        self.image = next(self.images_list)
        self.repaint_image()

    def zoom_in_action(self):
        print("zoomin")

    def zoom_out_action(self):
        print("zoomout")

    def rotate_action(self):
        print("rotate")

    def flip_action(self):
        print("flip")

    def fit_to_window(self):
        if self.actions.fit_to_window.isChecked():
            self.image_size_policy = 'fit_to_window'
        else:
            self.image_size_policy = 'fit_auto'

        self.actions.fit_to_width.setChecked(False)
        self.actions.fit_to_height.setChecked(False)
        self.actions.show_original_size.setChecked(False)

        self.repaint_image()

    def fit_to_width(self):
        if self.actions.fit_to_width.isChecked():
            self.image_size_policy = 'fit_to_width'
        else:
            self.image_size_policy = 'fit_auto'

        self.actions.fit_to_window.setChecked(False)
        self.actions.fit_to_height.setChecked(False)
        self.actions.show_original_size.setChecked(False)

        self.repaint_image()

    def fit_to_height(self):
        if self.actions.fit_to_height.isChecked():
            self.image_size_policy = 'fit_to_height'
        else:
            self.image_size_policy = 'fit_auto'

        self.actions.fit_to_window.setChecked(False)
        self.actions.fit_to_width.setChecked(False)
        self.actions.show_original_size.setChecked(False)

        self.repaint_image()

    def original_size(self):
        if self.actions.show_original_size.isChecked():
            self.image_size_policy = 'original_size'
        else:
            self.image_size_policy = 'fit_auto'

        self.actions.fit_to_window.setChecked(False)
        self.actions.fit_to_width.setChecked(False)
        self.actions.fit_to_height.setChecked(False)

        self.repaint_image()

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
            self._show_normal()
        else:
            self._show_fullscreen()

    def minimize_action(self):
        self.showMinimized()

    def maximize_action(self):
        if self.isMaximized():
            self._show_normal()
        else:
            self._show_maximized()

    def exit_action(self):
        if self.isFullScreen():
            self._show_normal()
        self._save_geometry()
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

    def repaint_image(self):
        w = self.centralWidget().width() - 2
        h = self.centralWidget().height() - 2
        pixmap = self.image.pixmap(self.image_size_policy, w, h)
        self.label.setPixmap(pixmap)

    def bar_log(self, msg):
        self.statusBar().showMessage(msg)

    def _show_normal(self):
        self.showNormal()
        self.actions.maximize.setIcon(self.app.ui.maximize_icon)
        self.actions.minimize.setVisible(True)
        self.actions.maximize.setVisible(True)
        self.repaint_image()

    def _show_maximized(self):
        self.showMaximized()
        self.actions.maximize.setIcon(self.app.ui.restore_icon)
        self.repaint_image()

    def _show_fullscreen(self):
        self.showFullScreen()
        self.actions.minimize.setVisible(False)
        self.actions.maximize.setVisible(False)
        self.repaint_image()

    def _save_geometry(self):
        geometry = self.saveGeometry()
        self.app.settings.set('viewer_window_geometry', geometry)

    def _restore_geometry(self):
        show_status_bar = self.app.settings.get('vui_show_status_bar', False, bool)
        load_geometry = self.app.settings.get('vui_save_window_geometry', False, bool)

        self.statusbar.setVisible(show_status_bar)

        if load_geometry:
            last_geometry = self.app.settings.get_value('viewer_window_geometry', '')
            try:
                self.restoreGeometry(last_geometry)
                if self.isMaximized():
                    self._show_maximized()
                else:
                    self._show_normal()
            except Exception:
                self._center_window()
        else:
            self._center_window()

        self.old_pos = self.pos()

    def _center_window(self):
        self.setFixedSize(self.app.ui.best_window_width, self.app.ui.best_window_height)
        frame_geometry = self.frameGeometry()
        frame_geometry.moveCenter(self.app.ui.screen_center)
        self.move(frame_geometry.topLeft())
