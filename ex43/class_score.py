class ClassScore(object):

    def __init__(self, num, message):
        self.num = num
        self.message = message

    def configure(self):
        return {'rating': self.num, 'message': self.message}
