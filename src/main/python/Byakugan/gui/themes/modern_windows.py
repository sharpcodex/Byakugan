from qtpy.QtCore import Qt, QMetaObject, Signal, Slot, QEvent
from qtpy.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QToolButton,
                            QLabel, QSizePolicy)


# noinspection PyPep8Naming
class ModernWindow(QWidget):
    def __init__(self, window, app_manager, parent=None):
        QWidget.__init__(self, parent)

        self.app = app_manager
        self._window = window
        self.vboxWindow = QVBoxLayout(self)
        self.windowFrame = QWidget(self)
        self.vboxFrame = QVBoxLayout(self.windowFrame)
        self.titleBar = WindowDragger(self, self.windowFrame)
        self.hboxTitle = QHBoxLayout(self.titleBar)
        self.lblTitle = QLabel('Title')
        self.btnMinimize = QToolButton(self.titleBar)
        self.btnRestore = QToolButton(self.titleBar)
        self.btnMaximize = QToolButton(self.titleBar)
        self.btnClose = QToolButton(self.titleBar)
        self.windowContent = QWidget(self.windowFrame)

        self.setup_ui()

        content_layout = QHBoxLayout()
        content_layout.setContentsMargins(0, 0, 0, 0)
        content_layout.addWidget(window)

        self.windowContent.setLayout(content_layout)

        self.setWindowTitle(window.windowTitle())
        self.setGeometry(window.geometry())

        self.installEventFilter(self)

        # Adding attribute to clean up the parent window when the child is closed
        self._window.setAttribute(Qt.WA_DeleteOnClose, True)
        self._window.destroyed.connect(self.__child_was_closed)

    def setup_ui(self):
        # create title bar, content
        self.vboxWindow.setContentsMargins(0, 0, 0, 0)

        self.windowFrame.setObjectName('windowFrame')

        self.vboxFrame.setContentsMargins(0, 0, 0, 0)

        self.titleBar.setObjectName('titleBar')
        self.titleBar.setSizePolicy(QSizePolicy(QSizePolicy.Preferred,
                                                QSizePolicy.Fixed))

        self.hboxTitle.setContentsMargins(0, 0, 0, 0)
        self.hboxTitle.setSpacing(0)

        self.lblTitle.setObjectName('lblTitle')
        self.lblTitle.setAlignment(Qt.AlignCenter)
        self.hboxTitle.addWidget(self.lblTitle)

        sp_buttons = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        self.btnMinimize.setObjectName('btnMinimize')
        self.btnMinimize.setSizePolicy(sp_buttons)
        self.hboxTitle.addWidget(self.btnMinimize)

        self.btnRestore.setObjectName('btnRestore')
        self.btnRestore.setSizePolicy(sp_buttons)
        self.btnRestore.setVisible(False)
        self.hboxTitle.addWidget(self.btnRestore)

        self.btnMaximize.setObjectName('btnMaximize')
        self.btnMaximize.setSizePolicy(sp_buttons)
        self.hboxTitle.addWidget(self.btnMaximize)

        self.btnClose.setObjectName('btnClose')
        self.btnClose.setSizePolicy(sp_buttons)
        self.hboxTitle.addWidget(self.btnClose)

        self.vboxFrame.addWidget(self.titleBar)

        self.vboxFrame.addWidget(self.windowContent)

        self.vboxWindow.addWidget(self.windowFrame)

        # set window flags
        self.setWindowFlags(
            Qt.Window | Qt.FramelessWindowHint | Qt.WindowSystemMenuHint)

        if self._window.app.qt_version >= (5,):
            self.setAttribute(Qt.WA_TranslucentBackground)

        # set stylesheet
        stylesheet = self.app.ui.get_stylesheet('frameless.qss')
        self.setStyleSheet(stylesheet)

        # automatically connect slots
        QMetaObject.connectSlotsByName(self)

    def __child_was_closed(self):
        self._window = None  # The child was deleted, remove the reference to it and close the parent window
        self.close()

    def eventFilter(self, source, event):
        if event.type() == QEvent.Close:
            if not self._window:
                return True
            return self._window.close()

        return QWidget.eventFilter(self, source, event)

    def setWindowTitle(self, title):
        super(ModernWindow, self).setWindowTitle(title)
        self.lblTitle.setText(title)

    @Slot()
    def on_btnMinimize_clicked(self):
        self.setWindowState(Qt.WindowMinimized)

    @Slot()
    def on_btnRestore_clicked(self):
        self.btnRestore.setVisible(False)
        self.btnMaximize.setVisible(True)
        self.setWindowState(Qt.WindowNoState)

    @Slot()
    def on_btnMaximize_clicked(self):
        self.btnRestore.setVisible(True)
        self.btnMaximize.setVisible(False)
        self.setWindowState(Qt.WindowMaximized)

    @Slot()
    def on_btnClose_clicked(self):
        self.close()

    @Slot()
    def on_titleBar_doubleClicked(self):
        if self.btnMaximize.isVisible():
            self.on_btnMaximize_clicked()
        else:
            self.on_btnRestore_clicked()


# noinspection PyUnresolvedReferences
class WindowDragger(QWidget):
    doubleClicked = Signal()

    def __init__(self, window, parent=None):
        QWidget.__init__(self, parent)
        self._window = window
        self._mousePressed = False
        self._mousePos = None
        self._windowPos = None

    def mousePressEvent(self, event):
        self._mousePressed = True
        self._mousePos = event.globalPos()
        self._windowPos = self._window.pos()

    def mouseMoveEvent(self, event):
        if self._mousePressed:
            self._window.move(self._windowPos +
                              (event.globalPos() - self._mousePos))

    def mouseReleaseEvent(self, event):
        self._mousePressed = False

    def mouseDoubleClickEvent(self, event):
        self.doubleClicked.emit()
