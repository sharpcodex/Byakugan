from fbs_runtime.application_context import cached_property
from qtpy.QtCore import Qt
from qtpy.QtWidgets import QAction


class WindowActions:
    def __init__(self, app_manager):
        self.app = app_manager

    @cached_property
    def previous(self):
        action = QAction(self.app.ui.previous_icon, "Previous")
        action.setToolTip("View Previous")
        action.setStatusTip("View Previous")
        action.setShortcuts(["Left", "PgUp"])
        action.setShortcutContext(Qt.ApplicationShortcut)
        return action

    @cached_property
    def next(self):
        action = QAction(self.app.ui.next_icon, "Next")
        action.setToolTip("View Next")
        action.setStatusTip("View Next")
        action.setShortcuts(["Right", "PgDown"])
        return action

    # --

    @cached_property
    def zoomin(self):
        action = QAction(self.app.ui.zoom_in_icon, "Zoom in")
        action.setToolTip("Zoom In")
        action.setStatusTip("Zoom In")
        action.setShortcuts(["Ctrl++", "Ctrl+=", "Up"])
        return action

    @cached_property
    def zoomout(self):
        action = QAction(self.app.ui.zoom_out_icon, "Zoom out")
        action.setToolTip("Zoom Out")
        action.setStatusTip("Zoom Out")
        action.setShortcuts(["Ctrl+-", "Ctrl+_", "Down"])
        return action

    @cached_property
    def rotate(self):
        action = QAction(self.app.ui.rotate_icon, "Rotate")
        action.setToolTip("Rotate Clockwise")
        action.setStatusTip("Rotate Clockwise")
        action.setShortcuts(["Ctrl+Down"])
        return action

    @cached_property
    def flip(self):
        action = QAction(self.app.ui.flip_icon, "Flip")
        action.setToolTip("Flip Horizontally")
        action.setStatusTip("Flip Horizontally")
        action.setShortcuts(["Ctrl+Right"])
        return action

    @cached_property
    def scale_w(self):
        action = QAction(self.app.ui.scale_w_icon, "Scale to width")
        action.setToolTip("Scale to Width")
        action.setStatusTip("Scale to Width")
        action.setShortcuts(["Shift+Right"])
        return action

    @cached_property
    def scale_h(self):
        action = QAction(self.app.ui.scale_h_icon, "Scale to Height")
        action.setToolTip("Scale to Height")
        action.setStatusTip("Scale to Height")
        action.setShortcuts(["Shift+Up"])
        return action

    @cached_property
    def scale(self):
        action = QAction(self.app.ui.scale_icon, "Scale to Fit")
        action.setToolTip("Scale to Fit")
        action.setStatusTip("Scale to Fit")
        action.setShortcuts(["Ctrl+0"])
        return action

    @cached_property
    def fullscreen(self):
        action = QAction(self.app.ui.fullscreen_icon, "Full Screen")
        action.setToolTip("Show in Fullscreen")
        action.setStatusTip("Show in Fullscreen")
        action.setShortcuts(["Alt+Return"])
        return action

    @cached_property
    def slideshow(self):
        action = QAction(self.app.ui.slideshow_icon, "Slide Show")
        action.setToolTip("Play Slideshow")
        action.setStatusTip("Play Slideshow")
        action.setShortcuts(["F11"])
        return action

    @cached_property
    def info(self):
        action = QAction(self.app.ui.info_icon, "Information")
        action.setToolTip("Show Information Window")
        action.setStatusTip("Show Information Window")
        action.setShortcuts(["Ctrl+I"])
        return action

    # --

    @cached_property
    def new(self):
        action = QAction(self.app.ui.new_icon, "New")
        action.setToolTip("New")
        action.setStatusTip("New")
        action.setShortcuts(["Ctrl+N"])
        return action

    @cached_property
    def open(self):
        action = QAction(self.app.ui.open_icon, "Open")
        action.setToolTip("Open")
        action.setStatusTip("Open")
        action.setShortcuts(["Ctrl+O"])
        return action

    @cached_property
    def save(self):
        action = QAction(self.app.ui.save_icon, "Save")
        action.setToolTip("Save")
        action.setStatusTip("Save")
        action.setShortcuts(["Ctrl+S"])
        return action

    @cached_property
    def save_as(self):
        action = QAction(self.app.ui.save_as_icon, "Save As")
        action.setToolTip("Save as")
        action.setStatusTip("Save as")
        action.setShortcuts(["Ctrl+Shift+S"])
        return action

    @cached_property
    def delete_item(self):
        action = QAction(self.app.ui.delete_icon, "Delete")
        action.setToolTip("Delete")
        action.setStatusTip("Delete")
        action.setShortcuts(["Del"])
        return action

    @cached_property
    def print(self):
        action = QAction(self.app.ui.print_icon, "Print")
        action.setToolTip("Print")
        action.setStatusTip("Print")
        action.setShortcuts(["Ctrl+P"])
        return action

    # --

    @cached_property
    def settings(self):
        action = QAction(self.app.ui.settings_icon, "Settings")
        action.setToolTip("Show Setting Window")
        action.setToolTip("Show Setting Window")
        action.setShortcuts(["Ctrl+,"])
        return action

    @cached_property
    def exit(self):
        action = QAction(self.app.ui.exit_icon, "E&xit")
        action.setToolTip("Exit")
        action.setToolTip("Exit")
        action.setShortcuts(["Escape"])
        return action
