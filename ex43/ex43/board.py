from random import randint
from class_score import ClassScore
STYLES = ['fomaie', 'long hog', 'short shredder']


class Board(object):

    def __init__(self, style=None):
        self.style = style or STYLES[randint(0, len(STYLES)-1)]

    def set_board(self):
        if self.style == 'foamie':
            cs = ClassScore(1, 'you can shred this, but look like a shoobie')
            return cs.configure()
        elif self.style == 'long hog':
            cs = ClassScore(2, 'hope you know what you\'re doing big kahuna')
            return cs.configure()
        elif self.style == 'short shredder':
            cs = ClassScore(3, 'shaka brah!')
            return cs.configure()
        else:
            cs = ClassScore(2, "oh that's neat, let it rip")

