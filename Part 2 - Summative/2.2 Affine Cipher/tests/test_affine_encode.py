from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import affine_encode

class TestAffineEncode(TestCase):
    keyword1 = "TEST"
    a1 = 3
    b1 = 9
    keyword2 = "CORGI"
    a2 = 5
    b2 = 15
    keyword3 = "BANANA"
    a3 = 7
    b3 = 12
    def test_affine_encode_no_space_upper_keyword1_a1_b1(self):
        self.assertEqual(affine_encode(self.keyword1, self.a1, self.b1), 'OVLO')
    def test_affine_encode_no_space_upper_keyword2_a1_b1(self):
        self.assertEqual(affine_encode(self.keyword2, self.a1, self.b1), 'PZIBH')
    def test_affine_encode_no_space_upper_keyword3_a1_b1(self):
        self.assertEqual(affine_encode(self.keyword3, self.a1, self.b1), 'MJWJWJ')

    def test_affine_encode_no_space_upper_keyword1_a2_b2(self):
        self.assertEqual(affine_encode(self.keyword1, self.a2, self.b2), 'GJBG')
    def test_affine_encode_no_space_upper_keyword2_a2_b2(self):
        self.assertEqual(affine_encode(self.keyword2, self.a2, self.b2), 'ZHWTD')
    def test_affine_encode_no_space_upper_keyword3_a2_b2(self):
        self.assertEqual(affine_encode(self.keyword3, self.a2, self.b2), 'UPCPCP')

    def test_affine_encode_no_space_upper_keyword1_a3_b3(self):
        self.assertEqual(affine_encode(self.keyword1, self.a3, self.b3), 'POIP')
    def test_affine_encode_no_space_upper_keyword2_a3_b3(self):
        self.assertEqual(affine_encode(self.keyword2, self.a3, self.b3), 'AGBCQ')
    def test_affine_encode_no_space_upper_keyword3_a3_b3(self):
        self.assertEqual(affine_encode(self.keyword3, self.a3, self.b3), 'TMZMZM')