import sys

from fbs_runtime.application_context.PyQt5 import ApplicationContext

from app_manager import AppManager
from dbs.config import Config
from windows.helpers.themes import Themer
from windows.main import MainWindow

if __name__ == '__main__':
    app_ctx = ApplicationContext()
    app_config = Config(app_ctx)
    app_manager = AppManager(app_ctx, app_config)

    window = MainWindow(app_manager)
    themed_window = Themer(app_manager).setup_theme(window)
    themed_window.show()

    exit_code = app_ctx.app.exec_()
    app_config.dispose()
    sys.exit(exit_code)
