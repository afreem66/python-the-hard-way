from random import randint
from class_score import ClassScore
SEASONS = ['fall', 'winter', 'spring', 'summer']


class Season(object):

    def __init__(self):
        self.season = SEASONS[randint(0, len(SEASONS)-1)]

        if self.season == 'fall' or self.season == 'winter':
            ClassScore(1, 'At least there aren\'t many people')
        else:
            ClassScore(1, 'Hey the water should be warm!')
