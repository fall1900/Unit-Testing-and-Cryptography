from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import sub_encode


class TestSubEncode(TestCase):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cipher_alphabet = "WJKUXVBMIYDTPLHZGONCRSAEFQ"
    cipher_alphabet1 = "QWERTYUIOPASDFGHJKLZXCVBNM"
    cipher_alphabet2 = "MNBVCXZLKJHGFDSAPOIUYTREWQ"

    def test_sub_encode_one_word_uppercase_alpha(self):
        self.assertEqual(sub_encode("HELLOWORLD", self.cipher_alphabet), "MXTTHAHOTU")

    def test_sub_encode_two_words_uppercase_alpha(self):
        self.assertEqual(sub_encode("HELLO WORLD", self.cipher_alphabet), "MXTTH AHOTU")

    def test_sub_encode_one_word_uppercase_alpha1(self):
        self.assertEqual(sub_encode("HELLOWORLD", self.cipher_alphabet1), "ITSSGVGKSR")

    def test_sub_encode_two_words_uppercase_alpha1(self):
        self.assertEqual(sub_encode("HELLO WORLD", self.cipher_alphabet1), "ITSSG VGKSR")

    def test_sub_encode_one_word_uppercase_alpha2(self):
        self.assertEqual(sub_encode("HELLOWORLD", self.cipher_alphabet2), "LCGGSRSOGV")

    def test_sub_encode_two_words_uppercase_alpha2(self):
        self.assertEqual(sub_encode("HELLO WORLD", self.cipher_alphabet2), "LCGGS RSOGV")
