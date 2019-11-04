from qtpy.QtCore import QCoreApplication, QSettings

ORGANIZATION_NAME = 'Thaka'
ORGANIZATION_DOMAIN = 'Thaka.sd'
APPLICATION_NAME = 'Byakugan'

QCoreApplication.setOrganizationName(ORGANIZATION_NAME)
QCoreApplication.setOrganizationDomain(ORGANIZATION_DOMAIN)
QCoreApplication.setApplicationName(APPLICATION_NAME)

settings = QSettings()
settings.setValue('t', True)
s = settings.value('t', type=bool)
print(s)
print(type(s))
# settings.clear()
