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
        self.assertEqual(self.tv.volume_level, 1)

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
        self.assertEqual(self.tv.volume_level, 1)

    def test_that_channel_up_works(self):
        self.tv = television.Television()
        self.tv.turn_on()
        self.tv.channel_up()
        self.assertEqual(self.tv.channel_level, 1)

    def test_that_channel_down_works(self):
        self.tv = television.Television()
        self.tv.turn_on()
        self.tv.channel_up()
        self.tv.channel_up()
        self.tv.channel_up()
        self.tv.channel_down()
        self.assertEqual(self.tv.channel_level, 2)

    def test_that_channel_setup_works(self):
        self.tv = television.Television()
        self.tv.turn_on()
        self.tv.channel_up()
        self.tv.set_channel_level(4)
        self.assertEqual(self.tv.channel_level, 4)

    def test_that_television_mutes(self):
        self.tv = television.Television()
        self.tv.turn_on()
        self.tv.volume_level = 50
        self.tv.mute_and_unmute_volume()
        self.assertEqual(self.tv.volume_level, 0)

    def test_that_television_unmutes(self):
        self.tv = television.Television()
        self.tv.turn_on()
        self.tv.volume_level = 75
        self.tv.mute_and_unmute_volume()
        self.tv.mute_and_unmute_volume()
        self.assertEqual(self.tv.volume_level, 75)

    def test_mute_when_tv_is_off_raises_error(self):
        self.tv = television.Television()
        self.tv.turn_off()
        with self.assertRaises(TelevisionError):
            self.tv.mute_and_unmute_volume()

    def test_volume_up_at_max(self):
        self.tv = television.Television()
        self.tv.turn_on()
        self.tv.volume_level = 100
        self.tv.volume_up()
        self.assertEqual(self.tv.volume_level, 100)

    def test_volume_down_at_min(self):
        self.tv = television.Television()
        self.tv.turn_on()
        self.tv.volume_level = 0
        self.tv.volume_down()
        self.assertEqual(self.tv.volume_level, 0)