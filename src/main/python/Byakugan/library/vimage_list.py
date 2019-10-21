from library.vimage import VImage
from helpers.path import PathHelpers


class VImageList:
    def __init__(self):
        self.images_list = None
        self.target_path = None
        self.target_list = None

    def from_path(self, target_path):
        self.target_path = target_path
        return self

    def from_list(self, target_list):
        self.target_list = target_list
        return self

    def __next__(self):
        if not self.images_list:
            self._build()
        return self.images_list.__next__()

    def __prev__(self):
        if not self.images_list:
            self._build()
        return self.images_list.__prev__()

    def __iter__(self):
        return self

    def _build(self):
        if self.target_path:
            images_list = [VImage(img) for img in PathHelpers().get_images_in_path(self.target_path)]
            self.images_list = CircularList(images_list)
        if self.target_list:
            images_list = [VImage(img) for img in self.target_list]
            self.images_list = CircularList(images_list)


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
