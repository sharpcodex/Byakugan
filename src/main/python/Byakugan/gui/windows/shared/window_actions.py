from fbs_runtime.application_context import cached_property
from qtpy.QtCore import Qt
from qtpy.QtWidgets import QAction, QSizePolicy, QWidget


class WindowActions:
    def __init__(self, app_manager):
        self.app = app_manager

    @cached_property
    def separator(self):
        separator = QWidget()
        separator.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        return separator

    @cached_property
    def previous(self):
        action = QAction(self.app.ui.previous_icon, "Previous")
        action.setToolTip("Previous")
        action.setStatusTip("View previous image, Shortcuts : Left, PgUp")
        action.setShortcuts(["Left", "PgUp"])
        action.setShortcutContext(Qt.ApplicationShortcut)
        return action

    @cached_property
    def next(self):
        action = QAction(self.app.ui.next_icon, "Next")
        action.setToolTip("Next")
        action.setStatusTip("View next image, Shortcuts : Right, PgDown")
        action.setShortcuts(["Right", "PgDown"])
        return action

    @cached_property
    def fit_to_window(self):
        action = QAction(self.app.ui.fit_to_window_icon, "Fit to window")
        action.setToolTip("Fit to window")
        action.setStatusTip("Fit image to window size, Shortcuts : Shift+Down")
        action.setShortcuts(["Shift+Down"])
        action.setCheckable(True)
        return action

    @cached_property
    def fit_to_width(self):
        action = QAction(self.app.ui.fit_to_width_icon, "Fit to width")
        action.setToolTip("Fit to width")
        action.setStatusTip("Fit image to window width, Shortcuts : Shift+Right")
        action.setShortcuts(["Shift+Right"])
        action.setCheckable(True)
        return action

    @cached_property
    def fit_to_height(self):
        action = QAction(self.app.ui.fit_to_height_icon, "Fit to height")
        action.setToolTip("Fit to height")
        action.setStatusTip("Fit image to window height, Shortcuts : Shift+Up")
        action.setShortcuts(["Shift+Up"])
        action.setCheckable(True)
        return action

    @cached_property
    def show_original_size(self):
        action = QAction(self.app.ui.show_original_size_icon, "Original Size")
        action.setToolTip("Original Size")
        action.setStatusTip("Show original image size, Shortcuts : Shift+Left")
        action.setShortcuts(["Shift+Left"])
        action.setCheckable(True)
        return action

    @cached_property
    def zoom_in(self):
        action = QAction(self.app.ui.zoom_in_icon, "Zoom in")
        action.setToolTip("Zoom in")
        action.setStatusTip("Zoom in, Shortcuts : Ctrl+Up, Ctrl++")
        action.setShortcuts(["Ctrl+Up", "Ctrl++", "Ctrl+="])
        return action

    @cached_property
    def zoom_out(self):
        action = QAction(self.app.ui.zoom_out_icon, "Zoom out")
        action.setToolTip("Zoom out")
        action.setStatusTip("Zoom out, Shortcuts : Ctrl+Down, Ctrl+-")
        action.setShortcuts(["Ctrl+Down", "Ctrl+-", "Ctrl+_"])
        return action

    @cached_property
    def rotate_right(self):
        action = QAction(self.app.ui.rotate_right_icon, "Rotate Clockwise")
        action.setToolTip("Rotate clockwise")
        action.setStatusTip("Rotate image clockwise, Shortcuts : Alt+Right")
        action.setShortcuts(["Alt+Right"])
        return action

    @cached_property
    def rotate_left(self):
        action = QAction(self.app.ui.rotate_left_icon, "Rotate Counterclockwise")
        action.setToolTip("Rotate counterclockwise")
        action.setStatusTip("Rotate image counterclockwise, Shortcuts : Alt+Left")
        action.setShortcuts(["Alt+Left"])
        return action

    @cached_property
    def flip_vertically(self):
        action = QAction(self.app.ui.flip_vertically_icon, "Flip Vertically")
        action.setToolTip("Flip vertically")
        action.setStatusTip("Flip image vertically, Shortcuts : Alt+Up")
        action.setShortcuts(["Alt+Up"])
        return action

    @cached_property
    def flip_horizontally(self):
        action = QAction(self.app.ui.flip_horizontally_icon, "Flip Horizontally")
        action.setToolTip("Flip horizontally")
        action.setStatusTip("Flip image horizontally, Shortcuts : Alt+Down")
        action.setShortcuts(["Alt+Down"])
        return action

    @cached_property
    def info(self):
        action = QAction(self.app.ui.info_icon, "Info")
        action.setToolTip("Image info")
        action.setStatusTip("Show image information window, Shortcuts : Ctrl+I")
        action.setShortcuts(["Ctrl+I"])
        return action

    @cached_property
    def new(self):
        action = QAction(self.app.ui.new_icon, "New")
        action.setToolTip("New")
        action.setStatusTip("Create new image, Shortcuts : Ctrl+N")
        action.setShortcuts(["Ctrl+N"])
        return action

    @cached_property
    def open(self):
        action = QAction(self.app.ui.open_icon, "Open")
        action.setToolTip("Open")
        action.setStatusTip("Open an existing image, Shortcuts : Ctrl+O")
        action.setShortcuts(["Ctrl+O"])
        return action

    @cached_property
    def save(self):
        action = QAction(self.app.ui.save_icon, "Save")
        action.setToolTip("Save")
        action.setStatusTip("Save changes, Shortcuts : Ctrl+S")
        action.setShortcuts(["Ctrl+S"])
        return action

    @cached_property
    def save_as(self):
        action = QAction(self.app.ui.save_as_icon, "Save As")
        action.setToolTip("Save as")
        action.setStatusTip("Save as new image, Shortcuts : Ctrl+Shift+S")
        action.setShortcuts(["Ctrl+Shift+S"])
        return action

    @cached_property
    def reload(self):
        action = QAction(self.app.ui.reload_icon, "Reload")
        action.setToolTip("Reload")
        action.setStatusTip("Reload file from disk, Shortcuts : Ctrl+R")
        action.setShortcuts(["Ctrl+R"])
        return action

    @cached_property
    def delete_item(self):
        action = QAction(self.app.ui.delete_icon, "Delete")
        action.setToolTip("Delete")
        action.setStatusTip("Delete, Shortcuts : Delete")
        action.setShortcuts(["Del"])
        return action

    @cached_property
    def print(self):
        action = QAction(self.app.ui.print_icon, "Print")
        action.setToolTip("Print")
        action.setStatusTip("Print, Shortcuts : Ctrl+P")
        action.setShortcuts(["Ctrl+P"])
        return action

    @cached_property
    def settings(self):
        action = QAction(self.app.ui.settings_icon, "Settings")
        action.setToolTip("Setting window")
        action.setToolTip("Show setting window, Shortcuts : Ctrl+,")
        action.setShortcuts(["Ctrl+,"])
        return action

    @cached_property
    def show_statusbar(self):
        action = QAction(self.app.ui.statusbar_icon, "Show Statusbar")
        action.setToolTip("Show Statusbar")
        action.setToolTip("Show Statusbar, Shortcuts : Ctrl+.")
        action.setShortcuts(["Ctrl+."])
        action.setCheckable(True)
        return action

    @cached_property
    def help(self):
        action = QAction(self.app.ui.help_icon, "Help")
        action.setToolTip("Help")
        action.setToolTip("Show help window, Shortcuts : F1")
        action.setShortcuts(["F1"])
        return action

    @cached_property
    def about(self):
        action = QAction(self.app.ui.about_icon, "About")
        action.setToolTip("About")
        action.setToolTip("About this application, Shortcuts : F2")
        action.setShortcuts(["F2"])
        return action

    @cached_property
    def slideshow(self):
        action = QAction(self.app.ui.slideshow_icon, "Slide Show")
        action.setToolTip("Slide Show")
        action.setStatusTip("Play slideshow, Shortcuts : Alt+Return, F11")
        action.setShortcuts(["Alt+Return", "F11"])
        action.setCheckable(True)
        return action

    @cached_property
    def minimize(self):
        action = QAction(self.app.ui.minimize_icon, "Minimize")
        action.setToolTip("Minimize")
        action.setStatusTip("Minimize")
        return action

    @cached_property
    def maximize(self):
        action = QAction(self.app.ui.maximize_icon, "Maximize")
        action.setToolTip("Maximize")
        action.setStatusTip("Maximize")
        return action

    @cached_property
    def exit(self):
        action = QAction(self.app.ui.exit_icon, "E&xit")
        action.setToolTip("Exit")
        action.setStatusTip("Exit, Shortcuts : Esc")
        action.setShortcuts(["Escape"])
        return action
