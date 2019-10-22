from fbs_runtime.application_context import cached_property
from qtpy.QtGui import QColor, QIcon
from qtpy.QtWidgets import QDesktopWidget
import qtawesome as qta

from app.defaults import *


class UiManager:
    def __init__(self, app_ctx, settings_manager):
        self.ctx = app_ctx
        self.settings = settings_manager

    # -------------- Icons -----------------------

    @cached_property
    def next_icon(self):
        return qta.icon('mdi.page-next-outline', color=self.color, color_active=self.active_color)

    @cached_property
    def previous_icon(self):
        return qta.icon('mdi.page-previous-outline', color=self.color, color_active=self.active_color)

    @cached_property
    def fit_to_window_icon(self):
        return qta.icon('mdi.fit-to-page-outline', color=self.color, color_active=self.active_color)

    @cached_property
    def fit_to_width_icon(self):
        return qta.icon('mdi.arrow-expand-horizontal', color=self.color, color_active=self.active_color)

    @cached_property
    def fit_to_height_icon(self):
        return qta.icon('mdi.arrow-expand-vertical', color=self.color, color_active=self.active_color)

    @cached_property
    def show_original_size_icon(self):
        return qta.icon('mdi.image-filter-center-focus-weak', color=self.color, color_active=self.active_color)

    @cached_property
    def zoom_in_icon(self):
        return qta.icon('mdi.magnify-plus-outline', color=self.color, color_active=self.active_color)

    @cached_property
    def zoom_out_icon(self):
        return qta.icon('mdi.magnify-minus-outline', color=self.color, color_active=self.active_color)

    @cached_property
    def rotate_right_icon(self):
        return qta.icon('mdi.axis-x-rotate-clockwise', color=self.color, color_active=self.active_color)

    @cached_property
    def rotate_left_icon(self):
        return qta.icon('mdi.axis-x-rotate-counterclockwise', color=self.color, color_active=self.active_color)

    @cached_property
    def flip_vertically_icon(self):
        return qta.icon('mdi.axis-y-rotate-clockwise', color=self.color, color_active=self.active_color)

    @cached_property
    def flip_horizontally_icon(self):
        return qta.icon('mdi.axis-z-rotate-clockwise', color=self.color, color_active=self.active_color)

    @cached_property
    def info_icon(self):
        return qta.icon('mdi.information-outline', color=self.color, color_active=self.active_color)

    @cached_property
    def new_icon(self):
        return qta.icon('mdi.folder-plus', color=self.color, color_active=self.active_color)

    @cached_property
    def open_icon(self):
        return qta.icon('mdi.folder-open', color=self.color, color_active=self.active_color)

    @cached_property
    def save_icon(self):
        return qta.icon('mdi.content-save-outline', color=self.color, color_active=self.active_color)

    @cached_property
    def save_as_icon(self):
        return qta.icon('mdi.content-save-move-outline', color=self.color, color_active=self.active_color)

    @cached_property
    def reload_icon(self):
        return qta.icon('mdi.sync', color=self.color, color_active=self.active_color)

    @cached_property
    def delete_icon(self):
        return qta.icon('mdi.delete', color=self.color, color_active=self.active_color)

    @cached_property
    def print_icon(self):
        return qta.icon('mdi.printer', color=self.color, color_active=self.active_color)

    @cached_property
    def settings_icon(self):
        return qta.icon('mdi.settings', color=self.color, color_active=self.active_color)

    @cached_property
    def help_icon(self):
        return qta.icon('mdi.help-rhombus-outline', color=self.color, color_active=self.active_color)

    @cached_property
    def slideshow_icon(self):
        return qta.icon('mdi.television-play', color=self.color, color_active=self.active_color)

    @cached_property
    def minimize_icon(self):
        return qta.icon('mdi.window-minimize', color=self.color, color_active=self.active_color)

    @cached_property
    def maximize_icon(self):
        return qta.icon('mdi.window-maximize', color=self.color, color_active=self.active_color)

    @cached_property
    def restore_icon(self):
        return qta.icon('mdi.window-restore', color=self.color, color_active=self.active_color)

    @cached_property
    def exit_icon(self):
        return qta.icon('mdi.window-close', color=self.color, color_active=self.active_color)

    @cached_property
    def window_icon(self):
        return QIcon(self.ctx.get_resource('images/main.png'))

    # -------------- Theme -----------------------
    @cached_property
    def app_theme(self):
        return self.settings.get('app_theme', DEFAULT_APP_THEME, str)

    @cached_property
    def app_color(self):
        return self.settings.get('app_color', DEFAULT_APP_COLOR, str)

    @cached_property
    def color(self):
        app_color = self.app_color
        if app_color == 'green':
            return QColor.fromHsv(123, 204, 198, 255)
        elif app_color == 'red':
            return QColor.fromHsv(0, 182, 252, 255)
        elif app_color == 'yellow':
            return QColor.fromHsv(38, 218, 253, 255)
        elif app_color == 'black':
            return QColor.fromHsv(0, 0, 0, 180)
        else:
            return QColor.fromHsv(0, 0, 255, 150)

    @cached_property
    def active_color(self):
        app_color = self.app_color
        if app_color == 'green':
            return QColor.fromHsv(123, 204, 148, 255)
        elif app_color == 'red':
            return QColor.fromHsv(0, 182, 202, 255)
        elif app_color == 'yellow':
            return QColor.fromHsv(38, 218, 203, 255)
        elif app_color == 'black':
            return QColor.fromHsv(0, 0, 0, 150)
        else:
            return QColor.fromHsv(0, 0, 255, 100)

    # -------------- Geometry -----------------------

    @cached_property
    def screen_center(self):
        return QDesktopWidget().availableGeometry().center()

    @cached_property
    def screen_width(self):
        screen_resolution = self.ctx.app.primaryScreen().availableGeometry()
        return screen_resolution.width()

    @cached_property
    def screen_height(self):
        screen_resolution = self.ctx.app.primaryScreen().availableGeometry()
        return screen_resolution.height()

    @cached_property
    def best_window_width(self):
        return self.screen_width * VUI_WINDOW_WIDTH_P

    @cached_property
    def best_window_height(self):
        return self.screen_height * VUI_WINDOW_HEIGHT_P

    # Helpers

    def get_stylesheet(self, sheet):
        with open(self.ctx.get_resource('themes/{}'.format(sheet))) as stylesheet:
            return stylesheet.read()
