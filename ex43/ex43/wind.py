from random import randint
from class_score import ClassScore
DIRECTIONS = {0: 'offshore', 1: 'onshore'}


class Wind(object):

    def __init__(self):
        self.direction = DIRECTIONS[randint(0, 1)]

    def set_wind(self):
        if self.direction == 'offshore':
            cs = ClassScore(1, 'offshore wind loooking righteous!')
            return cs.configure()
        else:
            cs = ClassScore(0, 'onshore wind will doe')
            return cs.configure()
