from unittest import TestCase

from package import television
from package.television import TelevisionError


class TestTelevision(TestCase):

    def test_that_television_turns_on(self):
        self.tv = television.Television()
        self.assertTrue(self.tv.is_on)

    def test_that_television_turns_off(self):
        self.tv = television.Television()
        self.tv.turn_off()
        self.assertFalse(self.tv.is_on)

    def test_that_increase_volume_works(self):
        self.tv = television.Television()
        self.tv.turn_on()
        self.tv.volume_up()
        self.assertEqual(self.tv.volume_level,1)

    def test_to_raise_Television_error(self):
        self.tv = television.Television()
        self.tv.turn_off()
        with self.assertRaises(TelevisionError):
            self.tv.volume_up()

    def test_that_decrease_volume_works(self):
        self.tv = television.Television()
        self.tv.turn_on()
        self.tv.volume_up()
        self.tv.volume_up()
        self.tv.volume_down()
        self.assertEqual(self.tv.volume_level,1)

    def test_that_channel_up_works(self):
        self.tv = television.Television()
        self.tv.turn_on()
        self.tv.channel_up()
        self.assertEqual(self.tv.channel_level,1)

    def test_that_channel_down_works(self):
        self.tv = television.Television()
        self.tv.turn_on()
        self.tv.channel_up()
        self.tv.channel_up()
        self.tv.channel_up()
        self.tv.channel_down()
        self.assertEqual(self.tv.channel_level,2)


    def test_that_channel_setup_works(self):
        self.tv = television.Television()
        self.tv.turn_on()
        self.tv.channel_up()
        self.tv.set_channel_level(4)
        self.assertEqual(self.tv.channel_level,4)
