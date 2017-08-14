from wave import Wave
from season import Season
from board import Board
from wind import Wind
from class_score import ClassScore


class Surf(object):

    def __init__(self):
        self.wave = Wave().set_wave()
        self.season = Season().set_season()
        self.board = Board().set_board()
        self.wind = Wind().set_wind()

    def shred(self):
        shred_score = ClassScore(self.score(), self.message()).configure()

        if shred_score['rating'] < 5:
            print(f"could be worse, here's what happend: {shred_score['message']}")
        elif shred_score['rating'] <= 10:
            print(f"way to go little grass hopper, look back on your gnar {shred_score['message']}")
        elif shred_score['rating'] >= 11:
            print(f"THE DUKE HAS RETURNED, bask in their glory {shred_score['message']}")
        else:
            print(f"whoa I don't know what happened, lets figure out {shred_score['message']}")

    def score(self):
        return self.wave['rating'] + self.season['rating'] + self.board['rating'] + self.wind['rating']

    def message(self):
        wave_message = self.wave['message']
        season_message = self.season['message']
        board_message = self.board['message']
        wind_message = self.wind['message']

        return """wave: {wave},
        season: {season},
        board: {board},
        wind: {wind} """.format(
            wave = wave_message,
            season = season_message,
            board = board_message,
            wind = wind_message)


s = Surf()
s.shred()
