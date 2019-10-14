import sys
import os
from pathlib import Path

from fbs_runtime.application_context.PyQt5 import ApplicationContext

from app.app_manager import AppManager
from gui.themes.theme_manager import ThemeManager
from gui.windows.main import MainWindow
from gui.windows.viewer import ViewerWindow
from helpers.images_list import ImagesList

TEST_VIEWER = True

if __name__ == '__main__':
    app_manager = AppManager(ApplicationContext())
    theme_manager = ThemeManager(app_manager)

    if len(sys.argv) > 1:
        target_image = sys.argv[1]
    elif TEST_VIEWER:
        target_image = str(Path.home() / 'testdata' / 'test-image.jpg')
    else:
        target_image = ''

    if os.path.isfile(target_image):
        window = ViewerWindow(app_manager, theme_manager, ImagesList([target_image]))
    else:
        window = MainWindow(app_manager, theme_manager)

    themed_window = theme_manager.setup(window)
    themed_window.show()

    exit_code = app_manager.exec()
    sys.exit(exit_code)
