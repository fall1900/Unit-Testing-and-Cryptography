from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import caesar_decode

class TestCaesarDecode(TestCase):
    shift = 6
    shift1 = 11
    shift2 = 27
    def test_caesar_decode_one_word_uppercase_alpha(self):
        self.assertEqual(caesar_decode("NKRRUCUXRJ", self.shift), "HELLOWORLD")

    def test_caesar_decode_two_words_uppercase_alpha(self):
        self.assertEqual(caesar_decode("NKRRU CUXRJ", self.shift), "HELLO WORLD")

    def test_caesar_decode_one_word_uppercase_alpha1(self):
        self.assertEqual(caesar_decode("SPWWZHZCWO", self.shift1), "HELLOWORLD")

    def test_caesar_decode_two_words_uppercase_alpha1(self):
        self.assertEqual(caesar_decode("SPWWZ HZCWO", self.shift1), "HELLO WORLD")

    def test_caesar_decode_one_word_uppercase_alpha2(self):
        self.assertEqual(caesar_decode("IFMMPXPSME", self.shift2), "HELLOWORLD")

    def test_caesar_decode_two_words_uppercase_alpha2(self):
        self.assertEqual(caesar_decode("IFMMP XPSME", self.shift2), "HELLO WORLD")
