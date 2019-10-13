import sys

from fbs_runtime.application_context.PyQt5 import ApplicationContext

from app_manager.app_manager import AppManager
from windows.main import MainWindow

if __name__ == '__main__':
    app_manager = AppManager(ApplicationContext())

    window = MainWindow(app_manager)
    themed_window = app_manager.theme.setup(window)
    themed_window.show()

    exit_code = app_manager.exec()
    sys.exit(exit_code)
