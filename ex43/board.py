from random import randint
from class_score import ClassScore
TYPES = ['fomaie', 'long hog', 'short shredder']


class Board(object):

    def __init__(self):
        self.type = TYPES[randint(0, len(TYPES)-1)]

        if self.type == 'foamie':
            ClassScore(1, 'you can shred this, but look like a shoobie')
        elif self.type == 'long hog':
            ClassScore(2, 'hope you know what you\'re doing big kahuna')
        else:
            ClassScore(3, 'shaka brah!')

