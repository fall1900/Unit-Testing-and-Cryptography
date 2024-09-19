from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import affine_decode

class TestAffineDecode(TestCase):
    keyword1 = "TEST"
    a1 = 3
    b1 = 9
    keyword2 = "CORGI"
    a2 = 5
    b2 = 15
    keyword3 = "BANANA"
    a3 = 7
    b3 = 12
    def test_affine_decode_no_space_upper_keyword1_a1_b1(self):
        self.assertEqual(affine_decode('OVLO', self.a1, self.b1), self.keyword1)
    def test_affine_decode_no_space_upper_keyword2_a1_b1(self):
        self.assertEqual(affine_decode('PZIBH', self.a1, self.b1), self.keyword2)
    def test_affine_decode_no_space_upper_keyword3_a1_b1(self):
        self.assertEqual(affine_decode('MJWJWJ', self.a1, self.b1), self.keyword3)

    def test_affine_decode_no_space_upper_keyword1_a2_b2(self):
        self.assertEqual(affine_decode('GJBG', self.a2, self.b2), self.keyword1)
    def test_affine_decode_no_space_upper_keyword2_a2_b2(self):
        self.assertEqual(affine_decode('ZHWTD', self.a2, self.b2), self.keyword2)
    def test_affine_decode_no_space_upper_keyword3_a2_b2(self):
        self.assertEqual(affine_decode('UPCPCP', self.a2, self.b2), self.keyword3)

    def test_affine_decode_no_space_upper_keyword1_a3_b3(self):
        self.assertEqual(affine_decode('POIP', self.a3, self.b3), self.keyword1)
    def test_affine_decode_no_space_upper_keyword2_a3_b3(self):
        self.assertEqual(affine_decode('AGBCQ', self.a3, self.b3), self.keyword2)
    def test_affine_decode_no_space_upper_keyword3_a3_b3(self):
        self.assertEqual(affine_decode('TMZMZM', self.a3, self.b3), self.keyword3)