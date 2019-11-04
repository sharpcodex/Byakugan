from fbs_runtime.application_context import cached_property
from qtpy.QtCore import QCoreApplication, QSettings

APPLICATION_NAME = 'Byakugan'

settings_dict = {
    # App Info
    'app_name': APPLICATION_NAME,
    'organization_domain': 'Thaka.sd',
    'organization_name': 'Thaka',
    # Theme
    'app_theme': 'Compact',  # Dark, Light, Compact or classic
    'app_color': 'Black',  # Red, Green, Glue, Yellow, Black or White
    'm_show_status_bar': False,  # True or False
    'm_save_window_geometry': False,  # True or False
    'v_show_status_bar': False,  # True or False
    'v_save_window_geometry': False,  # True or False
    'e_show_status_bar': False,  # True or False
    'e_save_window_geometry': False,  # True or False
}


class SettingsManager:
    def __init__(self):
        # settings config
        QCoreApplication.setApplicationName(settings_dict['app_name'])
        QCoreApplication.setOrganizationDomain(settings_dict['organization_domain'])
        QCoreApplication.setOrganizationName(settings_dict['organization_name'])

        self.settings = QSettings()
        # Fill defaults
        if self.settings.value('app_name', type=str) != settings_dict['app_name']:
            for key, value in settings_dict.items():
                self.set(key, value)

    def set(self, key, value):
        try:
            self.settings.setValue(key, value)
        except (QSettings.AccessError, QSettings.FormatError):
            pass  # TODO : log errors

    def get(self, key, default_value=None):
        default = default_value if default_value is not None else settings_dict[key]
        try:
            return self.settings.value(key, default)
        except (QSettings.AccessError, QSettings.FormatError):
            return default

    def read(self, key, default_value=None, value_type=str):
        try:
            return self.settings.value(key, default_value, type=value_type)
        except (QSettings.AccessError, QSettings.FormatError):
            return default_value

    def set_all(self, settings):
        for key, value in settings.items():
            self.set(key, value)

    def get_all(self):
        settings = {}
        for key, _ in settings_dict.items():
            settings[key] = self.get(key)
        return settings

    @cached_property
    def app_name(self):
        return self.get('app_name')

    @cached_property
    def app_theme(self):
        return self.get('app_theme')

    @cached_property
    def app_color(self):
        return self.get('app_color')
