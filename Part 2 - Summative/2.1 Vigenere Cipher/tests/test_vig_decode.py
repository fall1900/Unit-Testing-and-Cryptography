from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import vig_decode

class TestVigDecode(TestCase):
    keyword1 = "TEST"
    keyword2 = "CORGI"
    keyword3 = "BANANA"
    def test_vig_decode_one_word_upper_keyword1(self):
        self.assertEqual(vig_decode(''), '')
    def test_vig_decode_one_word_lower_keyword1(self):
        self.assertEqual(vig_decode(''), '')
    def test_vig_decode_two_words_keyword1(self):
        self.assertEqual(vig_decode(''), '')
    def test_vig_decode_one_word_upper_keyword2(self):
        self.assertEqual(vig_decode(''), '')
    def test_vig_decode_one_word_lower_keyword2(self):
        self.assertEqual(vig_decode(''), '')
    def test_vig_decode_two_words_keyword2(self):
        self.assertEqual(vig_decode(''), '')
    def test_vig_decode_one_word_upper_keyword3(self):
        self.assertEqual(vig_decode(''), '')
    def test_vig_decode_one_word_lower_keyword3(self):
        self.assertEqual(vig_decode(''), '')
    def test_vig_decode_two_words_upper_keyword3(self):
        self.assertEqual(vig_decode(''), '')