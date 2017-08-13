from random import randint
DIRECTIONS = {0: 'offshore', 1: 'onshore'}


class Wind(object):

    def __init__(self):
        self.direction = DIRECTIONS[randint(0, 1)]

        if self.direction == 'offshore':
            return 1
        else:
            return 0
