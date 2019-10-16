import sys
import os
from pathlib import Path

from fbs_runtime.application_context.PyQt5 import ApplicationContext

from app.settings_manager import SettingsManager
from app.ui_manager import UiManager
from app.app_manager import AppManager
from gui.themes.theme_manager import ThemeManager

TEST_VIEWER = True

if __name__ == '__main__':
    ctx = ApplicationContext()
    settings_manager = SettingsManager()
    ui_manager = UiManager(ctx, settings_manager)
    app_manager = AppManager(ctx, settings_manager, ui_manager)
    theme_manager = ThemeManager(app_manager)

    if len(sys.argv) > 1:
        target_image = sys.argv[1]
    elif TEST_VIEWER:
        target_image = str(Path.home() / 'testdata' / 'test-image.jpg')
    else:
        target_image = ''

    if os.path.isfile(target_image):
        from gui.windows.viewer import ViewerWindow
        from helpers.vimage_list import VImageList

        window = ViewerWindow(app_manager, VImageList([target_image]))
        window.show()
    else:
        from gui.windows.main import MainWindow

        window = MainWindow(app_manager)
        theme_manager.setup(window).show()

    sys.exit(ctx.app.exec_())
