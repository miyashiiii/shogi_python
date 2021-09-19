
class KomaType:
    available_moves = []

    def nari(self):
        raise NotImplementedError





class Fu(KomaType):
    available_moves = [
        (-1, 0)
    ]

    def nari(self):
        self.available_moves = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, 0),
        ]


class Kyosha(KomaType):
    available_moves = [
        (-8, 0),
        (-7, 0),
        (-6, 0),
        (-5, 0),
        (-4, 0),
        (-3, 0),
        (-2, 0),
        (-1, 0),
    ]

    def nari(self):
        self.available_moves = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, 0),
        ]


class Keima(KomaType):
    available_moves = [
        (-2, -1),
        (-2, 1)
    ]

    def nari(self):
        self.available_moves = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, 0),
        ]


class Gin(KomaType):
    available_moves = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (1, -1),
        (1, 1),
    ]

    def nari(self):
        self.available_moves = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, 0),
        ]


class Kin(KomaType):
    available_moves = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, 0),
    ]


class Kaku(KomaType):
    available_moves = [
    ]
    for i in range(9):
        if i == 0:
            available_moves.append((0, 0))
        minus = -i
        available_moves += [(i, i), (i, -i), (-i, i), (-i, -i)]

    def nari(self):
        self.available_moves += [
            (1, 0),
            (0, 1),
            (0, -1),
            (-1, 0),
        ]


class Hisha(KomaType):
    available_moves = [
    ]
    for i in range(9):
        available_moves += [(0, i), (0, -i), (i, 0), (i, 0)]

    def nari(self):
        self.available_moves += [
            (1, 1),
            (1, -1),
            (-1, 1),
            (-1, -1),

        ]


class Ou(KomaType):
    available_moves = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]
