import itertools


class ID:
    def __init__(self):
        self.recipe_id = itertools.count(start=1, step=1)

    def make_id(self):
        return next(self.recipe_id)
