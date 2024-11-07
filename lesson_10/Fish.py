import Animals


class Fish(Animals):

    def __init__(self, type_of_water, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type_of_water = type_of_water
