from fbs_runtime.application_context import cached_property
from qtpy.QtWidgets import QAction


class WindowActions:
    def __init__(self, app_manager):
        self.app = app_manager

    @cached_property
    def next(self):
        action = QAction(self.app.ui.next_icon, "&Next")
        action.setToolTip("View next")
        return action

    @cached_property
    def previous(self):
        action = QAction(self.app.ui.previous_icon, "&Previous")
        action.setToolTip("View previous")
        return action

    @cached_property
    def fullscreen(self):
        action = QAction(self.app.ui.fullscreen_icon, "&Full Screen")
        action.setToolTip("Show in fullscreen")
        return action

    @cached_property
    def slideshow(self):
        action = QAction(self.app.ui.slideshow_icon, "&Slide Show")
        action.setToolTip("Play slideshow")
        return action

    @cached_property
    def reload(self):
        action = QAction(self.app.ui.reload_icon, "&Reload")
        action.setToolTip("Reload from disk")
        return action

    @cached_property
    def exit(self):
        action = QAction(self.app.ui.exit_icon, "E&xit")
        action.setToolTip("Exit")
        return action
