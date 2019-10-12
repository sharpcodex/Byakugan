import sys
from fbs_runtime.application_context.PyQt5 import ApplicationContext
from fbs_runtime.application_context import cached_property
from windows.main_window import MainWindow

class AppContext(ApplicationContext):
    def setup():
        pass

    @cached_property
    def main_window(self):
        return MainWindow(self)

    def run(self):
        self.main_window.show()
        return self.app.exec_()

if __name__ == '__main__':
    app_ctxt = AppContext()
    exit_code = app_ctxt.run()
    sys.exit(exit_code)
