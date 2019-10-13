from fbs_runtime.application_context import cached_property
from PyQt5.QtGui import QIcon
import qtmodern.styles
import qtmodern.windows


class ThemeManager:
    def __init__(self, ctx, app_theme):
        self.ctx = ctx
        self.app_theme = app_theme

    def setup(self, window):
        if self.app_theme == 'modern':
            qtmodern.styles.dark(self.ctx.app)
            return qtmodern.windows.ModernWindow(window)
        else:
            return window

    @cached_property
    def window_icon(self):
        return QIcon(self.ctx.get_resource('images/main.png'))
