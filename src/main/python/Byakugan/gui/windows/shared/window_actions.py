from fbs_runtime.application_context import cached_property
from qtpy.QtWidgets import QAction


class WindowActions:
    def __init__(self, app_manager):
        self.app = app_manager

    @cached_property
    def full_screen_action(self):
        full_screen_action = QAction(self.app.ui.expand_icon, "Full Screen")
        full_screen_action.setToolTip("Show in full screen mode")
        full_screen_action.setStatusTip("Show in full screen mode")
        return full_screen_action

    @cached_property
    def exit_action(self):
        exit_action = QAction(self.app.ui.exit_icon, "&Exit")
        exit_action.setToolTip("Exit")
        exit_action.setStatusTip("Exit")
        return exit_action
