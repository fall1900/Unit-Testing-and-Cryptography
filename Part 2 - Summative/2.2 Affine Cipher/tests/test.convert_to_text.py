from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import convert_to_num

class TestConvertToNum(TestCase):
    keyword1 = "BARK"
    keyword2 = "TEST"
    keyword3 = "HELLOWORLD"

    def test_convert_to_num_no_space_upper_keyword1_a1_b1(self):
        self.assertEqual(convert_to_num('187253'), self.keyword1)
    def test_convert_to_num_no_space_upper_keyword2_a1_b1(self):
        self.assertEqual(convert_to_num(''), self.keyword2)
    def test_convert_to_num_no_space_upper_keyword3_a1_b1(self):
        self.assertEqual(convert_to_num(''), self.keyword3)