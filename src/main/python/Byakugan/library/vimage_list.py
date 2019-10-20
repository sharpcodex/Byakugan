from library.io import IO
from library.vimage import VImage


class VImageList:
    def __init__(self):
        self.images_list = CircularList([])

    def from_path(self, path):
        images_list = [VImage(img) for img in IO.get_images(path)]
        self.images_list = CircularList(images_list)
        return self

    def __next__(self):
        return self.images_list.__next__()

    def __prev__(self):
        return self.images_list.__prev__()

    def __iter__(self):
        return self


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
