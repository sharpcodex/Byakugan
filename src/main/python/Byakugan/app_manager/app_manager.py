from PyQt5 import QtCore

from app_manager.config_manager import ConfigManager
from app_manager.theme_manager import ThemeManager


class AppManager:
    def __init__(self, ctx):
        self.ctx = ctx
        self.config = ConfigManager(self.ctx.get_resource('dbs/config.db'))
        self.theme = ThemeManager(self.ctx, self.config.app_theme)

    def get_resource(self, path):
        return self.ctx.get_resource(path)

    def exec(self):
        exit_code = self.ctx.app.exec_()
        self.dispose()
        return exit_code

    def quit(self):
        self.dispose()
        QtCore.QCoreApplication.instance().quit()

    def dispose(self):
        self.config.dispose()
