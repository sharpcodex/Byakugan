from fbs_runtime.application_context import cached_property
from qtpy import QT_VERSION
from qtpy.QtCore import QCoreApplication


class AppManager:
    def __init__(self, ctx, settings_manager, ui_manager):
        self.ctx = ctx
        self.settings = settings_manager
        self.ui = ui_manager

    def get_resource(self, path):
        return self.ctx.get_resource(path)

    @staticmethod
    def quit():
        QCoreApplication.instance().quit()

    @cached_property
    def qt_version(self):
        return tuple(int(v) for v in QT_VERSION.split('.'))
