import Animals


class Cats(Animals):

    def __init__(self, is_wool: bool, wool_len: int | None, *args, **kwargs):
        self.is_wool = is_wool
        self.wool_len = wool_len if is_wool else 0
        super().__init__(*args, **kwargs)
