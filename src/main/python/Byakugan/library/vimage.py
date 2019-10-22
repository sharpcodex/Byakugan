from qtpy.QtCore import Qt
from qtpy.QtGui import QPixmap, QTransform


class VImage:
    def __init__(self, path):
        self.path = path
        self._image = None

    def zoom_in(self):
        if not self._image:
            self._load_image()
        new_size = self._image.size() + self._image.size() * 0.2
        self._image = self._image.scaled(new_size, Qt.KeepAspectRatio)

    def zoom_out(self):
        if not self._image:
            self._load_image()
        new_size = self._image.size() - self._image.size() * 0.2
        self._image = self._image.scaled(new_size, Qt.KeepAspectRatio)

    def rotate_right(self):
        if not self._image:
            self._load_image()
        transform90 = QTransform()
        transform90.rotate(90)
        self._image = self._image.transformed(transform90)

    def rotate_left(self):
        if not self._image:
            self._load_image()
        transform90 = QTransform()
        transform90.rotate(-90)
        self._image = self._image.transformed(transform90)

    def flip_vertically(self):
        if not self._image:
            self._load_image()
        transform90 = QTransform()
        transform90.scale(1, -1)
        self._image = self._image.transformed(transform90)

    def flip_horizontally(self):
        if not self._image:
            self._load_image()
        transform90 = QTransform()
        transform90.scale(-1, 1)
        self._image = self._image.transformed(transform90)

    def pixmap(self, size_policy, max_w, max_h):
        if not self._image:
            self._load_image()
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

    def reload(self):
        self._load_image()

    def _load_image(self):
        self._image = QPixmap(str(self.path))
