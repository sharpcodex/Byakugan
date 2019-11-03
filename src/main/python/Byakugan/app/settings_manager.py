from fbs_runtime.application_context import cached_property
from qtpy.QtCore import QCoreApplication, QSettings

SETTINGS_RESET = False
APPLICATION_NAME = 'Byakugan'

defaults = {

    'app_theme': 'modern-dark',  # modern-dark, modern-light,Compact or classic
    'app_color': 'black',  # red, green,blue, yellow, Black or White
    'app_name': 'Byakugan',
    'organization_name': 'Thaka',
    'organization_domain': 'Thaka.sd',
    'vui_show_status_bar': False,  # True or False
    'vui_save_window_geometry': False  # True or False
}


class SettingsManager:
    def __init__(self):
        QCoreApplication.setOrganizationName(defaults['organization_name'])
        QCoreApplication.setOrganizationDomain(defaults['organization_domain'])
        QCoreApplication.setApplicationName(APPLICATION_NAME)

        self.settings = QSettings()
        if self.settings.value('app_name', type=str) != APPLICATION_NAME or SETTINGS_RESET is True:
            for key, value in defaults.items():
                self.set(key, value)

    def set(self, key, value):
        try:
            self.settings.setValue(key, value)
        except (QSettings.AccessError, QSettings.FormatError):
            pass

    def get(self, key, default_value=None):
        default = default_value if default_value is not None else defaults[key]
        try:
            return self.settings.value(key, default)
        except (QSettings.AccessError, QSettings.FormatError):
            return default

    def read(self, key, default_value, value_type):
        try:
            return self.settings.value(key, default_value, type=value_type)
        except (QSettings.AccessError, QSettings.FormatError):
            return default_value

    @cached_property
    def app_name(self):
        return self.get('app_name')

    @cached_property
    def app_theme(self):
        return self.get('app_theme')

    @cached_property
    def app_color(self):
        return self.get('app_color')
