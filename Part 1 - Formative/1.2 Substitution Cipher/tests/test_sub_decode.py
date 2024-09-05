from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import sub_decode

class TestSubDecode(TestCase):
    cipher_alphabet = "WJKUXVBMIYDTPLHZGONCRSAEFQ"
    cipher_alphabet1 = "QWERTYUIOPASDFGHJKLZXCVBNM"
    cipher_alphabet2 = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
    def test_sub_decode_one_word_uppercase(self):
        self.assertEqual(sub_decode("MXTTHAHOTU", cipher_alphabet), "HELLOWORLD")

    def test_sub_decode_two_words_uppercase(self):
        self.assertEqual(sub_decode("MXTTH AHOTU", cipher_alphabet), "HELLO WORLD")

    def test_sub_decode_one_word_uppercase(self):
        self.assertEqual(sub_decode("MXTTHAHOTU", cipher_alphabet1), "HELLOWORLD")

    def test_sub_decode_two_words_uppercase(self):
        self.assertEqual(sub_decode("MXTTH AHOTU", cipher_alphabet1), "HELLO WORLD")

    def test_sub_decode_one_word_uppercase(self):
        self.assertEqual(sub_decode("MXTTHAHOTU", cipher_alphabet2), "HELLOWORLD")

    def test_sub_decode_two_words_uppercase(self):
        self.assertEqual(sub_decode("MXTTH AHOTU", cipher_alphabet2), "HELLO WORLD")