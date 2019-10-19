from fbs_runtime.application_context import cached_property
from qtpy.QtGui import QImage, QPixmap
import cv2

from helpers.io import IO


class VImage:
    def __init__(self, path):
        self.path = path

    def max_resize(self, max_width, max_height):
        height, width, channels = self._image.shape
        target_width = max_width if width > max_width else width
        target_height = max_height if height > max_height else height
        resized = cv2.resize(self._image, (target_width, target_height))
        return self._to_pixmap(resized)

    @staticmethod
    def _to_pixmap(image):
        if len(image.shape) == 3:
            if image.shape[2] == 4:
                qformat = QImage.Format_RGBA8888
            else:
                qformat = QImage.Format_RGB888
            qimage = QImage(image,
                            image.shape[1],
                            image.shape[0],
                            image.strides[0],  # <--- +++
                            qformat)
            qimage = qimage.rgbSwapped()
            return QPixmap.fromImage(qimage)
        else:
            return None

    @cached_property
    def _image(self):
        return IO.load_image(self.path)
