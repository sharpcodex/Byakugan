import sys

from fbs_runtime.application_context.PyQt5 import ApplicationContext

from app_manager import AppManager
from dbs.config import Config
from windows.main import MainWindow
from windows.themes import Themer

if __name__ == '__main__':
    ctx = ApplicationContext()
    config = Config(ctx)
    app = AppManager(ctx, config)

    window = Themer(app).setup_theme(MainWindow(app))
    window.show()

    exit_code = ctx.app.exec_()
    config.dispose()
    sys.exit(exit_code)
