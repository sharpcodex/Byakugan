class CircularList(object):
    def __init__(self, collection):
        self.collection = collection
        self.len = len(self.collection)
        self.index = -1

    def __next__(self):
        try:
            self.index += 1
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


l = CircularList([1, 2, 3])

print(l.__next__())
print(l.__next__())
print(l.__next__())

l = CircularList([1, 2, 3])

print(l.__prev__())
print(l.__prev__())
print(l.__prev__())

l = CircularList([1, 2, 3])
print(l.__next__())
print(l.__prev__())
print(l.__next__())
print(l.__next__())
print(l.__prev__())
print(l.__next__())
