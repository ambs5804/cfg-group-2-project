import itertools

# Class to assign unique IDs to objects


class ID:
    _counter = itertools.count()

    @classmethod
    def make_id(cls):
        return next(ID._counter)

    @classmethod
    def reset(cls, start=0):
        ID._counter = itertools.count(start)
