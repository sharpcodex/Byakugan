from qtpy.QtGui import QPalette, QColor

from gui.themes.modern_windows import ModernWindow


class ThemeManager:
    def __init__(self, app_manager):
        self.app = app_manager

    # Style
    def setup(self, window):
        app_theme = self.app.settings.app_theme
        if app_theme == 'modern-dark':
            self.apply_dark_theme()
            return ModernWindow(window, self.app)
        elif app_theme == 'modern-light':
            self.apply_light_theme()
            return ModernWindow(window, self.app)
        else:
            return window

    def apply_dark_theme(self):
        dark_palette = QPalette()
        # base
        dark_palette.setColor(QPalette.WindowText, QColor(180, 180, 180))
        dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.Light, QColor(180, 180, 180))
        dark_palette.setColor(QPalette.Midlight, QColor(90, 90, 90))
        dark_palette.setColor(QPalette.Dark, QColor(35, 35, 35))
        dark_palette.setColor(QPalette.Text, QColor(180, 180, 180))
        dark_palette.setColor(QPalette.BrightText, QColor(180, 180, 180))
        dark_palette.setColor(QPalette.ButtonText, QColor(180, 180, 180))
        dark_palette.setColor(QPalette.Base, QColor(42, 42, 42))
        dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.Shadow, QColor(20, 20, 20))
        dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        dark_palette.setColor(QPalette.HighlightedText, QColor(180, 180, 180))
        dark_palette.setColor(QPalette.Link, QColor(56, 252, 196))
        dark_palette.setColor(QPalette.AlternateBase, QColor(66, 66, 66))
        dark_palette.setColor(QPalette.ToolTipBase, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.ToolTipText, QColor(180, 180, 180))
        # disabled
        dark_palette.setColor(QPalette.Disabled, QPalette.WindowText,
                              QColor(127, 127, 127))
        dark_palette.setColor(QPalette.Disabled, QPalette.Text,
                              QColor(127, 127, 127))
        dark_palette.setColor(QPalette.Disabled, QPalette.ButtonText,
                              QColor(127, 127, 127))
        dark_palette.setColor(QPalette.Disabled, QPalette.Highlight,
                              QColor(80, 80, 80))
        dark_palette.setColor(QPalette.Disabled, QPalette.HighlightedText,
                              QColor(127, 127, 127))

        self.app.ctx.app.setPalette(dark_palette)
        self._apply_base_theme()

    def apply_light_theme(self):
        light_palette = QPalette()
        # base
        light_palette.setColor(QPalette.WindowText, QColor(0, 0, 0))
        light_palette.setColor(QPalette.Button, QColor(240, 240, 240))
        light_palette.setColor(QPalette.Light, QColor(180, 180, 180))
        light_palette.setColor(QPalette.Midlight, QColor(200, 200, 200))
        light_palette.setColor(QPalette.Dark, QColor(225, 225, 225))
        light_palette.setColor(QPalette.Text, QColor(0, 0, 0))
        light_palette.setColor(QPalette.BrightText, QColor(0, 0, 0))
        light_palette.setColor(QPalette.ButtonText, QColor(0, 0, 0))
        light_palette.setColor(QPalette.Base, QColor(237, 237, 237))
        light_palette.setColor(QPalette.Window, QColor(240, 240, 240))
        light_palette.setColor(QPalette.Shadow, QColor(20, 20, 20))
        light_palette.setColor(QPalette.Highlight, QColor(76, 163, 224))
        light_palette.setColor(QPalette.HighlightedText, QColor(0, 0, 0))
        light_palette.setColor(QPalette.Link, QColor(0, 162, 232))
        light_palette.setColor(QPalette.AlternateBase, QColor(225, 225, 225))
        light_palette.setColor(QPalette.ToolTipBase, QColor(240, 240, 240))
        light_palette.setColor(QPalette.ToolTipText, QColor(0, 0, 0))
        # disabled
        light_palette.setColor(QPalette.Disabled, QPalette.WindowText,
                               QColor(115, 115, 115))
        light_palette.setColor(QPalette.Disabled, QPalette.Text,
                               QColor(115, 115, 115))
        light_palette.setColor(QPalette.Disabled, QPalette.ButtonText,
                               QColor(115, 115, 115))
        light_palette.setColor(QPalette.Disabled, QPalette.Highlight,
                               QColor(190, 190, 190))
        light_palette.setColor(QPalette.Disabled, QPalette.HighlightedText,
                               QColor(115, 115, 115))

        self.app.ctx.app.setPalette(light_palette)
        self._apply_base_theme()

    def _apply_base_theme(self):
        if self.app.qt_version < (5,):
            self.app.ctx.app.setStyle('plastique')
        else:
            self.app.ctx.app.setStyle('Fusion')
        self.app.ctx.app.setStyleSheet(self.app.ui.get_stylesheet('style.qss'))
