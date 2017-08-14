from random import randint
from class_score import ClassScore
TYPES = ['fomaie', 'long hog', 'short shredder']


class Board(object):

    def __init__(self):
        self.type = TYPES[randint(0, len(TYPES)-1)]

    def set_board(self):
        if self.type == 'foamie':
            cs = ClassScore(1, 'you can shred this, but look like a shoobie')
            return cs.configure()
        elif self.type == 'long hog':
            cs = ClassScore(2, 'hope you know what you\'re doing big kahuna')
            return cs.configure()
        else:
            cs = ClassScore(3, 'shaka brah!')
            return cs.configure()

