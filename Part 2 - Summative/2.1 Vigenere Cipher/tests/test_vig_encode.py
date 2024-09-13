from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import vig_encode

class TestVigEncode(TestCase):
    keyword1 = "TEST"
    keyword2 = "CORGI"
    keyword3 = "BANANA"
    def test_vig_encode_no_space_upper_keyword1(self):
        self.assertEqual(vig_encode('NAHIDWIN', self.keyword1), 'FEZAW__F')
    def test_vig_encode_no_space_lower_keyword1(self):
        self.assertEqual(vig_encode('nahidwin', self.keyword1), 'FEZAW__F')
    def test_vig_encode_multiple_spaces_upper_keyword1(self):
        self.assertEqual(vig_encode('NAH_ID_WIN', self.keyword1), 'FEZSAHROAR')
    def test_vig_encode_no_space_upper_keyword2(self):
        self.assertEqual(vig_encode('NAHIDWIN', self.keyword2), 'POYOLYWD')
    def test_vig_encode_no_space_lower_keyword2(self):
        self.assertEqual(vig_encode('nahidwin', self.keyword2), 'POYOLYWD')
    def test_vig_encode_multiple_spaces_upper_keyword2(self):
        self.assertEqual(vig_encode('NAH_ID_WIN', self.keyword2), 'POYFQFNMOV')
    def test_vig_encode_no_space_upper_keyword3(self):
        self.assertEqual(vig_encode('NAHIDWIN', self.keyword3), 'OAUIQWJN')
    def test_vig_encode_no_space_lower_keyword3(self):
        self.assertEqual(vig_encode('nahidwin', self.keyword3), 'OAUIQWJN')
    def test_vig_encode_multiple_spaces_upper_keyword3(self):
        self.assertEqual(vig_encode('NAH_ID_WIN', self.keyword3), 'OAU_VDAWVN')