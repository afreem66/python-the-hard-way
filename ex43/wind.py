from random import randint
from class_score import ClassScore
DIRECTIONS = {0: 'offshore', 1: 'onshore'}


class Wind(object):

    def __init__(self):
        self.direction = DIRECTIONS[randint(0, 1)]

        if self.direction == 'offshore':
            ClassScore(1, 'offshore wind loooking righteous!')
        else:
            ClassScore(0, 'onshore wind will doe')
