from fbs_runtime.application_context import cached_property
from qtpy.QtGui import QColor, QIcon
import qtawesome as qta

from app.defaults import *


class UiManager:
    def __init__(self, app_ctx, settings_manager):
        self.ctx = app_ctx
        self.settings = settings_manager

    # Icons
    @cached_property
    def exit_icon(self):
        return qta.icon('mdi.exit-to-app', color=self.icon_color, color_active=self.active_icon_color)

    @cached_property
    def expand_icon(self):
        return qta.icon('fa5s.expand', color=self.icon_color, color_active=self.active_icon_color)

    @cached_property
    def window_icon(self):
        return QIcon(self.ctx.get_resource('images/main.png'))

    # Theme
    @cached_property
    def app_theme(self):
        return self.settings.getValue('app_theme', DEFAULT_APP_THEME, str)

    @cached_property
    def app_color(self):
        return self.settings.getValue('app_color', DEFAULT_APP_COLOR, str)

    @cached_property
    def icon_color(self):
        app_color = self.app_color
        if app_color == 'green':
            return QColor.fromHsv(123, 204, 198, 255)
        elif app_color == 'red':
            return QColor.fromHsv(0, 182, 252, 255)
        elif app_color == 'yellow':
            return QColor.fromHsv(38, 218, 253, 255)
        else:
            if self.app_theme == 'modern-dark':
                return QColor.fromHsv(0, 0, 255, 150)
            else:
                return QColor.fromHsv(0, 0, 0, 180)

    @cached_property
    def active_icon_color(self):
        app_color = self.app_color
        if app_color == 'green':
            return QColor.fromHsv(123, 204, 148, 255)
        elif app_color == 'red':
            return QColor.fromHsv(0, 182, 202, 255)
        elif app_color == 'yellow':
            return QColor.fromHsv(38, 218, 203, 255)
        else:
            if self.app_theme == 'modern-dark':
                return QColor.fromHsv(0, 0, 255, 100)
            else:
                return QColor.fromHsv(0, 0, 0, 150)

    # Geometry
    @cached_property
    def screen_width(self):
        screen_resolution = self.ctx.app.desktop().screenGeometry()
        return screen_resolution.width()

    @cached_property
    def screen_height(self):
        screen_resolution = self.ctx.app.desktop().screenGeometry()
        return screen_resolution.height()

    @cached_property
    def window_height(self):
        return self.screen_height * WINDOW_HEIGHT_P

    @cached_property
    def max_window_height(self):
        return self.screen_height * MAX_WINDOW_HEIGHT_P

    @cached_property
    def window_width(self):
        return self.screen_width * WINDOW_WIDTH_P

    @cached_property
    def max_window_width(self):
        return self.screen_width * MAX_WINDOW_WIDTH_P

    # Helpers

    def get_stylesheet(self, sheet):
        with open(self.ctx.get_resource('themes/{}'.format(sheet))) as stylesheet:
            return stylesheet.read()
