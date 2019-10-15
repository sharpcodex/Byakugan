import os
from qtpy.QtGui import QPixmap


class VImage:
    def __init__(self, path, pixmap):
        self.path = path
        self.pixmap = pixmap


class VImageList:
    def __init__(self, images_files_list):
        images_list = []
        for image_file in images_files_list:
            if os.path.isfile(image_file):
                pixmap = QPixmap(image_file)
                images_list.append(VImage(image_file, pixmap))

        self.images_list = iter(images_list)

    def get_next(self):
        return next(self.images_list)
