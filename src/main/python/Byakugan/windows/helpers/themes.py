import qtmodern.styles
import qtmodern.windows


class Themer:
    def __init__(self, app_manager):
        self.app_manager = app_manager

    def setup_theme(self, window):
        if self.app_manager.config.app_theme == 'modern':
            qtmodern.styles.dark(self.app_manager.ctx.app)
            return qtmodern.windows.ModernWindow(window)
        else:
            return window
