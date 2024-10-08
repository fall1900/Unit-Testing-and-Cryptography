from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import convert_to_text

class TestConvertToText(TestCase):
    keyword1 = "BARK"
    keyword2 = "TEST"
    keyword3 = "CANS"

    def test_convert_to_text_no_space_upper_keyword1_a1_b1(self):
        self.assertEqual(convert_to_text(187253, len(self.keyword1)), self.keyword1)
    def test_convert_to_text_no_space_upper_keyword2_a1_b1(self):
        self.assertEqual(convert_to_text(346235, len(self.keyword2)), self.keyword2)
    def test_convert_to_text_no_space_upper_keyword3_a1_b1(self):
        self.assertEqual(convert_to_text(325158,len(self.keyword3)), self.keyword3)