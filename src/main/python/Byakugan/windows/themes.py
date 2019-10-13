import qtmodern.styles
import qtmodern.windows


class Themer:
    def __init__(self, app):
        self.app = app

    def setup_theme(self, window):
        if self.app.config.app_theme == 'modern':
            qtmodern.styles.dark(self.app.ctx.app)
            return qtmodern.windows.ModernWindow(window)
        else:
            return window
