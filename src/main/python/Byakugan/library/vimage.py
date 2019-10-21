from fbs_runtime.application_context import cached_property
from qtpy.QtCore import Qt
from qtpy.QtGui import QPixmap


class VImage:
    def __init__(self, path):
        self.path = path

    def pixmap(self, size_policy, max_w, max_h):
        if size_policy == 'fit_auto':
            return self._image.scaled(max_w, max_h, Qt.KeepAspectRatio)
        elif size_policy == 'fit_to_window':
            return self._image.scaled(max_w, max_h)
        elif size_policy == 'fit_to_width':
            return self._image.scaledToWidth(max_w)
        elif size_policy == 'fit_to_height':
            return self._image.scaledToHeight(max_h)
        else:
            return self._image

    @cached_property
    def _image(self):
        image = QPixmap(str(self.path))
        return image
