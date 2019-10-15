from qtpy.QtCore import QCoreApplication, QSettings

from app.defaults import *


class SettingsManager:
    def __init__(self):
        QCoreApplication.setOrganizationName(ORGANIZATION_NAME)
        QCoreApplication.setOrganizationDomain(ORGANIZATION_DOMAIN)
        QCoreApplication.setApplicationName(APPLICATION_NAME)
        self.settings = QSettings()

        app_name = self.settings.value('app_name', type=str)
        if app_name != APPLICATION_NAME:
            self._fill_defaults()

    def setValue(self, key, value):
        self.settings.setValue(key, value)

    def getValue(self, key, default_value, value_type):
        return self.settings.value(key, default_value, type=value_type)

    def _fill_defaults(self):
        try:
            # App Info
            self.settings.setValue('app_name', APPLICATION_NAME)
            self.settings.setValue('organization_domain', ORGANIZATION_DOMAIN)
            self.settings.setValue('organization_name', ORGANIZATION_NAME)
            # Theme
            self.settings.setValue('app_theme', DEFAULT_APP_THEME)  # modern-dark, modern-light or classic
            self.settings.setValue('app_color', DEFAULT_APP_COLOR)  # green, red, yellow or classic
        except (QSettings.AccessError, QSettings.FormatError):
            from qtpy.QtWidgets import QMessageBox
            QMessageBox.critical(self, 'Fatal Error', 'Fatal Error')
