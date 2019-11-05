from fbs_runtime.application_context import cached_property
from qtpy.QtCore import QCoreApplication, QSettings

# App Info Keys
APP_NAME = 'app_name'
ORGANIZATION_DOMAIN = 'organization_domain'
ORGANIZATION_NAME = 'organization_name'
# Theme
APP_THEME = 'app_theme'
APP_COLOR = 'app_color'
M_SHOW_STATUS_BAR = 'm_show_status_bar'
M_SAVE_WINDOW_GEOMETRY = 'm_save_window_geometry'
V_SHOW_STATUS_BAR = 'v_show_status_bar'
V_SAVE_WINDOW_GEOMETRY = 'v_save_window_geometry'
E_SHOW_STATUS_BAR = 'e_show_status_bar'
E_SAVE_WINDOW_GEOMETRY = 'e_save_window_geometry'
VIEWER_WINDOW_GEOMETRY = 'viewer_window_geometry'

# Defaults
APPLICATION_NAME = 'Byakugan'
DEFAULT_SETTINGS = {
    # App Info
    APP_NAME: APPLICATION_NAME,
    ORGANIZATION_DOMAIN: 'Thaka.sd',
    ORGANIZATION_NAME: 'Thaka',
    # Theme
    APP_THEME: 'Compact',  # Dark, Light, Compact or classic
    APP_COLOR: 'Black',  # Red, Green, Yellow, Black or White
    M_SHOW_STATUS_BAR: False,  # True or False
    M_SAVE_WINDOW_GEOMETRY: False,  # True or False
    V_SHOW_STATUS_BAR: False,  # True or False
    V_SAVE_WINDOW_GEOMETRY: False,  # True or False
    E_SHOW_STATUS_BAR: False,  # True or False
    E_SAVE_WINDOW_GEOMETRY: False,  # True or False
}


class SettingsManager:
    def __init__(self):
        # settings config
        QCoreApplication.setApplicationName(DEFAULT_SETTINGS[APP_NAME])
        QCoreApplication.setOrganizationDomain(DEFAULT_SETTINGS[ORGANIZATION_DOMAIN])
        QCoreApplication.setOrganizationName(DEFAULT_SETTINGS[ORGANIZATION_NAME])

        self.settings = QSettings()

        # Fill defaults
        if self.settings.value(APP_NAME, type=str) != DEFAULT_SETTINGS[APP_NAME]:
            for key, value in DEFAULT_SETTINGS.items():
                self.set(key, value)

    def set(self, key, value):
        try:
            self.settings.setValue(key, value)
        except (QSettings.AccessError, QSettings.FormatError):
            pass  # TODO : log errors

    def set_all(self, settings):
        for key, value in settings.items():
            self.set(key, value)

    def get(self, key, default_value=None):
        if default_value is None and key in DEFAULT_SETTINGS.keys():
            default_value = DEFAULT_SETTINGS[key]
        try:
            value = self.settings.value(key, default_value)
            if type(value) == str and value.lower() in ('true', 'false'):
                return self._str2bool(value)
            return value
        except (QSettings.AccessError, QSettings.FormatError):
            return default_value

    def get_all(self):
        settings = {}
        for key, _ in DEFAULT_SETTINGS.items():
            settings[key] = self.get(key)
        return settings

    def read(self, key, default_value=None, value_type=str):
        try:
            return self.settings.value(key, default_value, type=value_type)
        except (QSettings.AccessError, QSettings.FormatError):
            return default_value

    def get_viewer_settings(self):
        viewer_settings = [VIEWER_WINDOW_GEOMETRY,
                           V_SHOW_STATUS_BAR,
                           V_SAVE_WINDOW_GEOMETRY]
        settings = {}
        for key in viewer_settings:
            settings[key] = self.get(key)
        return settings

    @staticmethod
    def _str2bool(st):
        return st.lower() in ("true", "yes", "1")
