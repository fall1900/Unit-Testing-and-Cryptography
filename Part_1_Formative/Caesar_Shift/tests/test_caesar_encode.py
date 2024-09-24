from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import caesar_encode

class TestCaesarEncode(TestCase):
    shift = 6
    shift1 = 11
    shift2 = 27
    def test_caesar_encode_one_word_uppercase_alpha(self):
        self.assertEqual(caesar_encode("HELLOWORLD", self.shift), "NKRRUCUXRJ")

    def test_caesar_encode_two_words_uppercase_alpha(self):
        self.assertEqual(caesar_encode("HELLO WORLD", self.shift), "NKRRU CUXRJ")

    def test_caesar_encode_one_word_uppercase_alpha1(self):
        self.assertEqual(caesar_encode("HELLOWORLD", self.shift1), "SPWWZHZCWO")

    def test_caesar_encode_two_words_uppercase_alpha1(self):
        self.assertEqual(caesar_encode("HELLO WORLD", self.shift1), "SPWWZ HZCWO")

    def test_caesar_encode_one_word_uppercase_alpha2(self):
        self.assertEqual(caesar_encode("HELLOWORLD", self.shift2), "IFMMPXPSME")

    def test_caesar_encode_two_words_uppercase_alpha2(self):
        self.assertEqual(caesar_encode("HELLO WORLD", self.shift2), "IFMMP XPSME")
