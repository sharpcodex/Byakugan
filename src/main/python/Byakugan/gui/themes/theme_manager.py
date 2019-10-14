from fbs_runtime.application_context import cached_property
from qtpy.QtGui import QPalette, QColor, QIcon
import qtawesome as qta

from gui.themes.modern_windows import ModernWindow


class ThemeManager:
    def __init__(self, app_manager):
        self.app = app_manager

    def setup(self, window):
        if self.app.config.app_theme == 'modern-dark':
            self.apply_dark_theme()
            return ModernWindow(window)
        elif self.app.config.app_theme == 'modern-light':
            self.apply_light_theme()
            return ModernWindow(window)
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
        self.app.ctx.app.setStyleSheet(self.get_stylesheet('style.qss'))

    def get_stylesheet(self, sheet):
        with open(self.app.get_resource('themes/{}'.format(sheet))) as stylesheet:
            return stylesheet.read()

    @cached_property
    def expand_icon(self):
        return qta.icon('fa5s.expand',
                        active='fa5s.expand',
                        color=self.icon_color,
                        color_active=self.active_icon_color)

    @cached_property
    def window_icon(self):
        return QIcon(self.app.get_resource('images/main.png'))

    @cached_property
    def icon_color(self):
        if self.app.config.app_color == 'green':
            return QColor.fromHsv(123, 204, 198, 255)
        elif self.app.config.app_color == 'red':
            return QColor.fromHsv(0, 182, 252, 255)
        elif self.app.config.app_color == 'yellow':
            return QColor.fromHsv(38, 218, 253, 255)
        else:
            if self.app.config.app_theme == 'modern-dark':
                return QColor.fromHsv(0, 0, 255, 150)
            else:
                return QColor.fromHsv(0, 0, 0, 180)

    @cached_property
    def active_icon_color(self):
        if self.app.config.app_color == 'green':
            return QColor.fromHsv(123, 204, 148, 255)
        elif self.app.config.app_color == 'red':
            return QColor.fromHsv(0, 182, 202, 255)
        elif self.app.config.app_color == 'yellow':
            return QColor.fromHsv(38, 218, 203, 255)
        else:
            if self.app.config.app_theme == 'modern-dark':
                return QColor.fromHsv(0, 0, 255, 100)
            else:
                return QColor.fromHsv(0, 0, 0, 150)
