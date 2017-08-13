from wave import Wave
from season import Season
from board import Board
from wind import Wind
from class_score import ClassScore


class Surf(object):

    def __init__(self):
        self.wave = Wave()
        self.season = Season()
        self.board = Baard()
        self.wind = Wind()

    def shred(self):
        shred_score = ClassScore(score(), message())

        if shred_score.score < 5:
            print(f"could be worse, here's what happend: {shred_score.message}")
        elif shred_score <= 10:
            print(f"way to go little grass hopper, look back on your gnar {shred_score.message}")
        elif shred_score >= 11:
            print(f"THE DUKE HAS RETURNED, bask in their glory {shred_score.message}")
        else:
            print(f"whoa I don't know what happened, lets figure out {shred_score.message}")

    def score(self):
        # loop through attrs and add up score

    def message(self):
        # loop thorugh the attrs and create message
