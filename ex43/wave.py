from random import randint
from class_score import ClassScore
SHAPES = ['mushy', 'sledge', 'curl']


class Wave(object):

    def __init__(self):
        self.speed = randint(0, 10)
        self.shape = SHAPES[randint(0, len(SHAPES)-1)]

        if self.speed <= 3 and self.shape == 'mushy':
            ClassScore(0, 'not even worth it today')
        elif self.speed <= 3:
            ClassScore(1, 'passable, brah!')
        elif self.speed < 8 and self.shape == 'sledge':
            ClassScore(2, 'gnarly dudeeee')
        elif self.speed > 8 and self.shape == 'curl':
            ClassScore(3, 'hang ten my ma, the waves are fine')
        else:
            ClassScore(1, 'global warming')

