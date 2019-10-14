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
