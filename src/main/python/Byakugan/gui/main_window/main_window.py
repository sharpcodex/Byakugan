from src.main.python.byakugan.gui.main_window.ui_main_window import Ui_Mainindow
from PyQt5.QtWidgets import QMainWindow


class MainWindow(QMainWindow, Ui_Mainindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
