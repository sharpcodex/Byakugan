from fbs_runtime.application_context import cached_property
from qtpy.QtGui import QImage, QPixmap
import cv2

from library.io import IO


class VImage:
    def __init__(self, path):
        self.path = path

    def pixmap(self, size_policy, max_w, max_h):
        (img_h, img_w) = self._image.shape[:2]

        if size_policy not in ['scale_w', 'scale_h', 'scale']:
            if img_w > max_w and img_h < max_h:
                size_policy = 'scale_w'
            elif img_w < max_w and img_h > max_h:
                size_policy = 'scale_h'
            elif img_w > max_w and img_h > max_h:
                if img_w > img_h:
                    size_policy = 'scale_w'
                else:
                    size_policy = 'scale_h'
        dim = self._get_dims(size_policy, img_w, img_h, max_w, max_h)
        resized = cv2.resize(self._image, dim, interpolation=cv2.INTER_AREA)
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
                            image.strides[0],
                            qformat)
            qimage = qimage.rgbSwapped()
            return QPixmap.fromImage(qimage)
        else:
            return None

    @staticmethod
    def _get_dims(size_policy, img_width, img_height, max_width, max_height):
        if size_policy == 'scale_w':
            r = max_width / float(img_width)
            dim = (max_width, int(img_height * r))
        elif size_policy == 'scale_h':
            r = max_height / float(img_height)
            dim = (int(img_width * r), max_height)
        elif size_policy == 'scale':
            dim = (max_width, max_height)
        else:
            dim = (img_width, img_height)
        return dim

    @cached_property
    def _image(self):
        return IO.load_image(self.path)
