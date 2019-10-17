import os
from qtpy.QtGui import QPixmap
from itertools import cycle
from pathlib import Path


class ImageList:
    def __init__(self):
        self.images_list = CircularList([])

    def from_path(self, path):
        images_files_list = []
        images_list = []

        path = Path(path)
        if path.is_file():
            path = path.parents[0]
        if path.is_dir():
            images_files_list = list(path.glob('*.jpg'))

        for image_file in images_files_list:
            print(image_file)
            pixmap = QPixmap(str(image_file))
            images_list.append(Image(image_file, pixmap))

        self.images_list = CircularList(images_list)

        return self

    def get_next(self):
        return self.images_list.__next__()

    def get_prev(self):
        return self.images_list.__prev__()


class Image:
    def __init__(self, path, pixmap):
        self.path = path
        self.pixmap = pixmap


class CircularList(object):
    def __init__(self, collection):
        self.collection = collection
        self.len = len(self.collection)
        self.index = -1

    def __next__(self):
        try:
            if self.index < self.len - 1:
                self.index += 1
            else:
                self.index = 0
            return self.collection[self.index]
        except IndexError:
            raise StopIteration

    def __prev__(self):
        try:
            if self.index > 0:
                self.index -= 1
            else:
                self.index = self.len - 1
            return self.collection[self.index]
        except IndexError:
            raise StopIteration

    def __iter__(self):
        return self
