from fbs_runtime.application_context.PyQt5 import ApplicationContext
from fbs_runtime.application_context import cached_property
from PyQt5.QtWidgets import QMainWindow

import sys

class AppContext(ApplicationContext):
    def setup():
        pass

    @cached_property
    def main_window(self):
        return QMainWindow()

    def run(self):
        self.main_window.resize(250, 150)
        self.main_window.show()
        return self.app.exec_()

if __name__ == '__main__':
    app_ctxt = AppContext()
    exit_code = app_ctxt.run()
    sys.exit(exit_code)
