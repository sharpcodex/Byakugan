from fbs_runtime.application_context import cached_property
import qtpy
from qtpy.QtCore import QCoreApplication

from app.config_manager import ConfigManager


class AppManager:
    def __init__(self, ctx):
        self.ctx = ctx
        self.config = ConfigManager(self.ctx.get_resource('dbs/config.db'))

    def get_resource(self, path):
        return self.ctx.get_resource(path)

    def exec(self):
        exit_code = self.ctx.app.exec_()
        self.dispose()
        return exit_code

    def quit(self):
        self.dispose()
        QCoreApplication.instance().quit()

    def dispose(self):
        self.config.dispose()

    @cached_property
    def qt_version(self):
        return tuple(int(v) for v in qtpy.QT_VERSION.split('.'))
