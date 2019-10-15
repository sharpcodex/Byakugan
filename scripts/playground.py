from fbs_runtime.application_context.PyQt5 import ApplicationContext
from qtpy.QtCore import QCoreApplication
from qtpy.QtWidgets import QMessageBox, QMainWindow

import pymsgbox

pymsgbox.alert(text='', title='', button='OK')
