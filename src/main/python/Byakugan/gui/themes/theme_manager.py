from fbs_runtime.application_context import cached_property
from qtpy.QtGui import QIcon

import qtmodern.styles
import qtmodern.windows


class ThemeManager:
    def __init__(self, app_manager):
        self.app = app_manager

    def setup(self, window):
        if self.app.config.app_theme == 'modern':
            qtmodern.styles.dark(self.app.ctx.app)
            return qtmodern.windows.ModernWindow(window)
        else:
            return window

    @cached_property
    def window_icon(self):
        return QIcon(self.app.get_resource('images/main.png'))
