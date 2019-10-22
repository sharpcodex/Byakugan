from qtpy.QtCore import Qt
from qtpy.QtGui import QPixmap, QTransform

DEFAULT_POLICY = {"zoom": 0, "rotate": 0, "flip_v": 0, "flip_h": 0}


class VImage:
    def __init__(self, path):
        self.path = path
        self._image = None
        self.image_policy = DEFAULT_POLICY.copy()

    def zoom_in(self):
        self.image_policy["zoom"] += 1

    def zoom_out(self):
        self.image_policy["zoom"] -= 1

    def rotate_right(self):
        self.image_policy["rotate"] += 1

    def rotate_left(self):
        self.image_policy["rotate"] -= 1

    def flip_vertically(self):
        self.image_policy["flip_v"] += 1

    def flip_horizontally(self):
        self.image_policy["flip_h"] += 1

    def pixmap(self, viewer_policy, max_w, max_h):
        if not self._image:
            self._load_image()

        image = self._image

        # Scale
        scale = viewer_policy["scale"]
        if scale == 'fit_auto':
            image = image.scaled(max_w, max_h, Qt.KeepAspectRatio)
        elif scale == 'fit_to_window':
            image = image.scaled(max_w, max_h)
        elif scale == 'fit_to_width':
            image = image.scaledToWidth(max_w)
        elif scale == 'fit_to_height':
            image = image.scaledToHeight(max_h)
        # Else Original

        # Zoom
        zoom = self.image_policy["zoom"]
        if zoom != 0:
            new_size = image.size()
            if zoom > 0:
                for i in range(abs(zoom)):
                    new_size *= 1.3
            else:
                for i in range(abs(zoom)):
                    new_size /= 1.3
            image = image.scaled(new_size, Qt.KeepAspectRatio)

        # Vertical Flipping
        v_flipping = (abs(self.image_policy["flip_v"]) % 2) * (1 if self.image_policy["flip_v"] >= 0 else -1)
        if v_flipping != 0:
            v_transform = QTransform().scale(1, -1)
            image = image.transformed(v_transform)

        # Horizontal Flipping
        h_flipping = (abs(self.image_policy["flip_h"]) % 2) * (1 if self.image_policy["flip_h"] >= 0 else -1)
        if h_flipping != 0:
            h_transform = QTransform().scale(-1, 1)
            image = image.transformed(h_transform)

        # Rotation
        rotation = 90 * (abs(self.image_policy["rotate"]) % 4) * (1 if self.image_policy["rotate"] >= 0 else -1)
        if rotation != 0:
            r_transform = QTransform().rotate(rotation)
            image = image.transformed(r_transform)

        return image

    def reload(self):
        self.image_policy = DEFAULT_POLICY.copy()
        self._load_image()

    def _load_image(self):
        self._image = QPixmap(str(self.path))
