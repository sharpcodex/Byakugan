import sys
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

    target_image = None
    if len(sys.argv) > 1:
        target_image = sys.argv[1]
    elif TEST_VIEWER:
        target_image = str(Path.home() / 'testdata' / 'test-image-1.jpg')

    if target_image:
        from gui.windows.viewer import ViewerWindow
        from library.vimage_list import VImageList

        window = ViewerWindow(app_manager, VImageList().from_path(target_image))
    else:
        from gui.windows.main import MainWindow

        window = MainWindow(app_manager)

    theme_manager.setup(window).show()

    sys.exit(ctx.app.exec_())
