import sys

from fbs_runtime.application_context.PyQt5 import ApplicationContext

from app_manager import AppManager
from dbs.config_manager import Config
from gui.main_window.main_window import MainWindow

if __name__ == '__main__':
    app_ctx = ApplicationContext()
    app_config = Config(app_ctx)
    app = AppManager(app_ctx, app_config)

    main_window = MainWindow(app)
    main_window.show()

    exit_code = app_ctx.app.exec_()
    app_config.close()
    sys.exit(exit_code)
