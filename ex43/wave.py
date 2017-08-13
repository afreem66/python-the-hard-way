from random import randint
SHAPES = ['mushy', 'sledge', 'curl']


class Wave(object):

    def __init__(self):
        self.speed = randint(0, 10)
        self.shape = SHAPES[randint(0, len(SHAPES)-1)]

        if self.speed <= 3 and self.shape == 'mushy':
            self.wave_rating(0, 'not even worth it today')
        elif self.speed <= 3:
            self.wave_rating(1, 'passable, brah!')
        elif self.speed < 8 and self.shape == 'sledge':
            self.wave_rating(2, 'gnarly dudeeee')
        elif self.speed > 8 and self.shape == 'curl':
            self.wave_rating(3, 'hang ten my ma, the waves are fine')
        else:
            self.wave_rating(1, 'global warming')

    def wave_rating(self, num, message):
        return {'rating': num, 'message': message}
