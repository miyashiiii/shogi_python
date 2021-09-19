import teban
from koma import Koma
from koma_type import Kyosha, Keima, Gin, Kin, Ou, Hisha, Kaku, Fu
from teban import Teban


class GameMaster:
    def __init__(self):
        self.board=[[
            Koma(Kyosha,Teban.GOTE),
            Koma(Keima,Teban.GOTE),
            Koma(Gin,Teban.GOTE),
            Koma(Kin,Teban.GOTE),
            Koma(Ou,Teban.GOTE),
            Koma(Kin,Teban.GOTE),
            Koma(Gin,Teban.GOTE),
            Koma(Keima,Teban.GOTE),
            Koma(Kyosha,Teban.GOTE),
        ],
            [Koma(),Koma(Hisha,Teban.GOTE),Koma(),Koma(),Koma(),Koma(),Koma(),Koma(Kaku,Teban.GOTE),Koma()],
            [Koma(Fu,Teban.GOTE)]*9,
            [Koma()]*9,
            [Koma()]*9,
            [Koma()]*9,

            [Koma(Fu,Teban.SENTE)]*9,
            [Koma(),Koma(Kaku,Teban.SENTE),Koma(),Koma(),Koma(),Koma(),Koma(),Koma(Hisha,Teban.SENTE),Koma()],
            [
            Koma(Kyosha,Teban.SENTE),
            Koma(Keima,Teban.SENTE),
            Koma(Gin,Teban.SENTE),
            Koma(Kin,Teban.SENTE),
            Koma(Ou,Teban.SENTE),
            Koma(Kin,Teban.SENTE),
            Koma(Gin,Teban.SENTE),
            Koma(Keima,Teban.SENTE),
            Koma(Kyosha,Teban.SENTE),
        ],
        ]

        self.motigoma_sente=[]
        self.motigoma_gote=[]

    def print_cui(self):
        koma_char_dict={
            Fu:"歩",
            Kyosha:"香",
            Keima:"桂",
            Gin:"銀",
            Kin:"金",
            Hisha:"飛",
            Kaku:"角",
            Ou:"王",
            None:"　"
        }
        for row in self.board:
            row_str=""
            for koma in row:
                koma_char = koma_char_dict[koma.koma_type]
                if koma.teban == Teban.GOTE:
                    koma_char = '\033[31m'+koma_char+'\033[0m'
                row_str += koma_char

            print(row_str)

game_master = GameMaster()
game_master.print_cui()
