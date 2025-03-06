from unittest import TestCase
import seven_segment

class TestSevenSegment(TestCase):
    def test_display_digit_0(self):
        seven_segment.display_digit("0")

    def test_display_digit_1(self):
        seven_segment.display_digit("1")

    def test_display_digit_2(self):
        seven_segment.display_digit("2")

    def test_display_digit_3(self):
        seven_segment.display_digit("3")

    def test_display_digit_4(self):
        seven_segment.display_digit("4")

    def test_display_digit_5(self):
        seven_segment.display_digit("5")

    def test_display_digit_6(self):
        seven_segment.display_digit("6")

    def test_display_digit_7(self):
        seven_segment.display_digit("7")

    def test_display_digit_8(self):
        seven_segment.display_digit("8")

    def test_display_digit_9(self):
        seven_segment.display_digit("9")

    def test_invalid_digit(self):
        seven_segment.display_digit("a")