from random import randint
from class_score import ClassScore
SHAPES = ['mushy', 'sledge', 'curl']


class Wave(object):

    def __init__(self, speed=None, shape=None):
        self.speed = speed or randint(0, 10)
        self.shape = shape or SHAPES[randint(0, len(SHAPES)-1)]

    def set_wave(self):
        if self.speed <= 3 and self.shape == 'mushy':
            cs = ClassScore(0, 'not even worth it today')
            return cs.configure()
        elif self.speed <= 3:
            cs = ClassScore(1, 'passable, brah!')
            return cs.configure()
        elif self.speed < 8 and self.shape == 'sledge':
            cs = ClassScore(2, 'gnarly dudeeee')
            return cs.configure()
        elif self.speed > 8 and self.shape == 'curl':
            cs = ClassScore(3, 'hang ten my ma, the waves are fine')
            return cs.configure()
        else:
            cs = ClassScore(1, 'global warming')
            return cs.configure()
