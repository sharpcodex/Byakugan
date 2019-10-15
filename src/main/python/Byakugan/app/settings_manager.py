import sys

from qtpy.QtCore import QCoreApplication, QSettings

from app.defaults import *


class SettingsManager:
    def __init__(self):
        QCoreApplication.setOrganizationName(ORGANIZATION_NAME)
        QCoreApplication.setOrganizationDomain(ORGANIZATION_DOMAIN)
        QCoreApplication.setApplicationName(APPLICATION_NAME)

        try:
            self.settings = QSettings()
            if self.settings.value('app_name', type=str) != APPLICATION_NAME:
                self._fill_defaults()
        except (QSettings.AccessError, QSettings.FormatError):
            SettingsManager.error_box()

    def set(self, key, value):
        try:
            self.settings.setValue(key, value)
        except (QSettings.AccessError, QSettings.FormatError):
            SettingsManager.error_box()

    def get(self, key, default_value, value_type):
        try:
            return self.settings.value(key, default_value, type=value_type)
        except (QSettings.AccessError, QSettings.FormatError):
            SettingsManager.error_box()

    def _fill_defaults(self):
        # App Info
        self.settings.setValue('app_name', APPLICATION_NAME)
        self.settings.setValue('organization_domain', ORGANIZATION_DOMAIN)
        self.settings.setValue('organization_name', ORGANIZATION_NAME)
        # Theme
        self.settings.setValue('app_theme', DEFAULT_APP_THEME)  # modern-dark, modern-light or classic
        self.settings.setValue('app_color', DEFAULT_APP_COLOR)  # green, red, yellow or classic

    @staticmethod
    def error_box():
        from qtpy.QtWidgets import qApp
        import pymsgbox
        pymsgbox.alert(text='can not access settings file, try to reinstall the application',
                       title='Fatal Error',
                       button='Exit')
        qApp.quit()
        sys.exit(-1)
