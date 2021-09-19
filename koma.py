



class Koma:
    def __init__(self, koma_type=None, teban=None):
        if (teban is None) != (koma_type is None):
            raise ValueError
        self.teban = teban
        self.koma_type = koma_type
