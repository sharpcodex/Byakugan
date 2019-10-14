import sys

from fbs_runtime.application_context.PyQt5 import ApplicationContext

from app.app_manager import AppManager
from gui.themes.theme_manager import ThemeManager
from gui.windows.main import MainWindow

if __name__ == '__main__':
    app_manager = AppManager(ApplicationContext())
    theme_manager = ThemeManager(app_manager)

    window = MainWindow(app_manager, theme_manager)
    themed_window = theme_manager.setup(window)
    themed_window.show()

    exit_code = app_manager.exec()
    sys.exit(exit_code)
