from nose.tools import *
from ex43.wave import Wave


def test_wave():
    wave = Wave(3, 'mushy')
    wave_two = Wave()

    assert_equal(wave.speed,  3)
    assert_equal(wave.shape, 'mushy')
    assert(wave_two.speed >= 0)
    assert(wave_two.speed <= 10)


def test_set_wave():
    wave = Wave(3, 'mushy')
    wave_two = Wave(10, 'curl')
    message = score(0, 'not even worth it today')
    message_two = score(3, 'hang ten my ma, the waves are fine')

    assert_equal(wave.set_wave(), message)
    assert_equal(wave_two.set_wave(), message_two)


def score(rating, message):
    return {'rating': rating, 'message': message}

