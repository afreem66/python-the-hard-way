from random import randint
from class_score import ClassScore
SEASONS = ['fall', 'winter', 'spring', 'summer']


class Season(object):

    def __init__(self):
        self.season = SEASONS[randint(0, len(SEASONS)-1)]

    def set_season(self):
        if self.season == 'fall' or self.season == 'winter':
            cs = ClassScore(1, 'At least there aren\'t many people')
            return cs.configure()
        else:
            cs = ClassScore(1, 'Hey the water should be warm!')
            return cs.configure()
